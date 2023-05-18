# tagifai/main.py
import logging
import warnings
from argparse import Namespace
from pathlib import Path
import pandas as pd
from config import config
# import utils

from tagifai import data, train, utils



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

def train_model(args_fp):
    """Train a model given arguments."""
    # Load labeled data
    df = pd.read_csv(Path(config.DATA_DIR, "labeled_projects.csv"))

    # Train
    args = Namespace(**utils.load_dict(filepath=args_fp))
    artifacts = train.train(df=df, args=args)
    performance = artifacts["performance"]
    print(json.dumps(performance, indent=2))


# tagifai/main.py
import mlflow
from numpyencoder import NumpyEncoder
import optuna
from optuna.integration.mlflow import MLflowCallback

def optimize(study_name, num_trials):
    """Optimize hyperparameters."""
    # Load labeled data
    df = pd.read_csv(Path(config.DATA_DIR, "labeled_projects.csv"))

    # Optimize
    args = Namespace(**utils.load_dict(filepath=args_fp))
    pruner = optuna.pruners.MedianPruner(n_startup_trials=5, n_warmup_steps=5)
    study = optuna.create_study(study_name="optimization", direction="maximize", pruner=pruner)
    mlflow_callback = MLflowCallback(
        tracking_uri=mlflow.get_tracking_uri(), metric_name="f1")
    study.optimize(
        lambda trial: train.objective(args, df, trial),
        n_trials=num_trials,
        callbacks=[mlflow_callback])

    # Best trial
    trials_df = study.trials_dataframe()
    trials_df = trials_df.sort_values(["user_attrs_f1"], ascending=False)
    utils.save_dict({**args.__dict__, **study.best_trial.params}, args_fp, cls=NumpyEncoder)
    print(f"\nBest value (f1): {study.best_trial.value}")
    print(f"Best hyperparameters: {json.dumps(study.best_trial.params, indent=2)}")
