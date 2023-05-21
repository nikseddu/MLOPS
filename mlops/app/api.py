from fastapi import FastAPI, Request

#For creating endpoints
from http import HTTPStatus
from typing import Dict

#For adding information to the response
from functools import wraps
from datetime import datetime


from tagifai import main
from config.config import logger
from config import config
from pathlib import Path


#Define Application
app =  FastAPI(title="TagiFai",
               description="Classier ML Model",
               version="0.1")


# @app.on_event("startup")
# def load_artifacts():
#     global artifacts
#     run_id = open(Path(config.CONFIG_DIR, "run_id.txt")).read()
#     artifacts = main.load_artifacts(model_dir=config.MODEL_DIR)
#     logger.info("Ready for inference!")



def construct_response(f):
    """Construct a JSON response for an endpoint."""

    @wraps(f)
    def wrap(request: Request, *args, **kwargs) -> Dict:
        results = f(request, *args, **kwargs)
        response = {
            "message": results["message"],
            "method": request.method,
            "status-code": results["status-code"],
            "timestamp": datetime.now().isoformat(),
            "url": request.url._url,
        }
        if "data" in results:
            response["data"] = results["data"]
        return response

    return wrap


@app.get("/",tags=["General"])
@construct_response
def _index(request: Request) -> Dict:
    """Health check."""
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {},
    }
    return response

@app.get("/performance", tags=["Performance"])
@construct_response
def _performance(request: Request, filter: str = None) -> Dict:
    """Get the performance metrics."""
    performance = artifacts["performance"]
    data = {"performance":performance.get(filter, performance)}
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": data,
    }
    return response
