import os
from pathlib import Path

import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s: ')

package_name = "covidClassifier"

list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipynb",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    
]

for file_path in list_of_files:
    file_path = Path(file_path)
    
    filedir, filename = os.path.split(file_path)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory : {filedir} for file: {filename}")
        
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass # create empty file
        logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{filename} already exists")