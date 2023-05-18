from pathlib import Path
BASE_DIR = Path(__file__).parent.parent.absolute()
CONFIG_DIR =Path(BASE_DIR,"Config")
DATA_DIR=Path(BASE_DIR,"data")

# Create dirs
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Assets
PROJECTS_URL = "https://raw.githubusercontent.com/GokuMohandas/Made-With-ML/main/datasets/projects.csv"
TAGS_URL = "https://raw.githubusercontent.com/GokuMohandas/Made-With-ML/main/datasets/tags.csv"

# config/config.py
STOPWORDS = [   "i",
    "me",
    "my",
   
    "won't",
    "wouldn",
    "wouldn't"]


# config/config.py
import mlflow
STORES_DIR = Path(BASE_DIR, "stores")
MODEL_REGISTRY = Path(STORES_DIR, "model")
MODEL_REGISTRY.mkdir(parents=True, exist_ok=True)
mlflow.set_tracking_uri("file://" + str(MODEL_REGISTRY.absolute()))
