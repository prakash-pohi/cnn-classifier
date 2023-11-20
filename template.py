import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO , format='[%(asctime)s: %(message)s]')

projectname = 'cnnClassifier'

file_list = [
    ".github/workflows/,gitkeep",
    f"src/{projectname}/__init__.py",
    f"src/{projectname}/components/__init__.py",
    f"src/{projectname}/entity/__init__.py",
    f"src/{projectname}/constants/__init__.py",
    f"src/{projectname}/config/__init__.py",
    f"src/{projectname}/pipeline/__init__.py",
    f"src/{projectname}/utils/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.yaml",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in file_list:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir , exist_ok=True)
        logging.info(f"creating file directory : {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"creating empty file : {filepath}")
        
    else:
        logging.info(f"{filepath} already exist")

