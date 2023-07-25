"""
    Simple python scipt to set up project structure for new, similar projects.
"""

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Base project name for folders
projectName = "classifier"

# List of files/folders to create
filesList = [
    ".github/workflows/.gitkeep",
    f"src/{projectName}/__init__.py",
    f"src/{projectName}/components/__init__.py",
    f"src/{projectName}/utils/__init__.py",
    f"src/{projectName}/config/__init__.py",
    f"src/{projectName}/config/configuration.py",
    f"src/{projectName}/pipeline/__init__.py",
    f"src/{projectName}/entity/__init__.py",
    f"src/{projectName}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "static/styles.css",
    "app.py"
]

for path in filesList:
    path = Path(path)
    filedir, filename = os.path.split(path)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for {path}")

    if (not os.path.exists(path)) or (os.path.getsize(path) == 0):
        with open(path, "w") as f:
            logging.info(f"Creating empty file {path}")
    else:
        logging.info(f"{path} already exists")