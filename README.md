# MLOPS
https://madewithml.com/


# Making Virtual Envrionement
```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install pip setuptools wheel
python3 -m pip install -e .
```

# Running App
```bash
uvicorn app.api:app --host 0.0.0.0 --port 8000 --reload --reload-dir tagifai --reload-dir app  # dev
gunicorn -c app/gunicorn.py -k uvicorn.workers.UvicornWorker app.api:app  # prod
```