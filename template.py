"""
template.py

Purpose:
    Automates the creation of project folders and files for the "thesis" project.
    This script will scaffold a predefined project structure with folders and files.
    Existing files won't be overwritten.

Usage:
    Run this script in the desired location to scaffold the project structure.
    `python template.py`

Dependencies:
    - os, pathlib, logging
"""

import os
from pathlib import Path
import logging

# Logging setup to track the creation of directories and files.
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "thesis"

# GitHub Workflow: Contains configurations for GitHub actions that manage CI/CD.
list_of_files = [
    ".github/workflows/.gitkeep",
]

# App Code: Contains the main application logic and source code, organized modularly.
list_of_files.extend([
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/models/__init__.py",
    f"src/{project_name}/models/params.yaml"
    f"src/{project_name}/streaming/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/config/config.yaml"
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/tests/__init__.py",
    f"src/{project_name}/logging/__init__.py",
    
    # Configuration files at the root level
    "params.yaml",
    "schema.yaml",
    
    # Primary application execution files
    "main.py",
    "app.py",
    "setup.py",
    "requirements.txt"
])

# Data: Contains the  dataset and any other necessary datasets.
list_of_files.extend([
    "data/.gitkeep",
])

# Research: Contains notebooks and other scripts for exploratory work.
list_of_files.extend([
    "research/00_read_data.ipynb"
])

# Docker: Configuration files for creating containerized versions of the application.
list_of_files.extend([
    "Dockerfile",
    ".dockerignore",
])

# Iterating through the list to create directories and files
for file_path_str in list_of_files:
    file_path = Path(file_path_str)
    
    # Create directory if it doesn't exist
    if file_path.parent and not file_path.parent.exists():
        file_path.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"Creating directory: {file_path.parent}")

    # Create the file if it's non-existent or empty
    if not file_path.exists() or file_path.stat().st_size == 0:
        file_path.touch()
        logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{file_path.name} already exists")