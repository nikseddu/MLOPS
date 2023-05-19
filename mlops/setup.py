# setup.py
from pathlib import Path

from setuptools import find_namespace_packages, setup

# Load packages from reequirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [line.strip() for line in file.readlines()]


# setup

# setup.py
docs_packages = ["mkdocs==1.3.0", "mkdocstrings==0.18.1"]

style_packages = ["black==22.3.0", "flake8==3.9.2", "isort==5.10.1"]

setup(
    name="tagifai",
    version="0.1",
    description="Classify  machine learning projects",
    author="Nikhil",
    url="https://nikseddu.github.io",
    python_requires=">=3.7",
    install_requires=[required_packages],
    extras_require={
        "dev": docs_packages + style_packages,
        "docs": docs_packages,
    },
)
