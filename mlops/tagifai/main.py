# tagifai/main.py
import logging
import warnings
from argparse import Namespace
from pathlib import Path
import pandas as pd
from config import config
from tagifai import utils

warnings.filterwarnings("ignore")

def elt_data():
    """Extract, load and transform our data assets."""
    # Extract + Load
    projects = pd.read_csv(config.PROJECTS_URL)
    tags = pd.read_csv(config.TAGS_URL)
    projects.to_csv(Path(config.DATA_DIR, "projects.csv"), index=False)
    tags.to_csv(Path(config.DATA_DIR, "tags.csv"), index=False)

    # Transform
    df = pd.merge(projects, tags, on="id")
    df = df[df.tag.notnull()]  # drop rows w/ no tag
    df.to_csv(Path(config.DATA_DIR, "labeled_projects.csv"), index=False)

    # logger.info("✅ Saved data!")

# tagifai/main.py
import json

from tagifai import data, train, utils


def train_model(args_fp):
    """Train a model given arguments."""
    # Load labeled data
    df = pd.read_csv(Path(config.DATA_DIR, "labeled_projects.csv"))

    # Train
    args = Namespace(**utils.load_dict(filepath=args_fp))
    artifacts = train.train(df=df, args=args)
    performance = artifacts["performance"]
    print(json.dumps(performance, indent=2))



if __name__ == "__main__":
    args_fp = Path(config.CONFIG_DIR, "args.json")
    train_model(args_fp)