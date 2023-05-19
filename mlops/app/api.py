from fastapi import FastAPI

#For creating endpoints
from http import HTTPStatus
from typing import Dict


#Define Application
app =  FastAPI(title="TagiFai",
               description="Classier ML Model",
               version="0.1")



@app.get("/")
def _index() -> Dict:
    """
    Health Check
    """
    response={
         "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {}
    }

    return response