import os
import shutil
import tomllib
import re

class projectExists(Exception):
    'Raised when a project of that name already exists.'
    def __init__(self, project_name:str) -> None:
        msg = f'{project_name} already exists'
        super().__init__(msg)

class projectMissing(Exception):
    'Raised when a project of that name does not exist.'
    def __init__(self, project_name:str) -> None:
        msg = f'{project_name} cannot be found'
        super().__init__(msg)

def make_pathsafe(project_name:str) -> str:
    project_name_pathsafe = project_name.strip()
    project_name_pathsafe = re.sub(r'[^a-zA-Z0-9_. -]', '', project_name_pathsafe)
    project_name_pathsafe = re.sub(r'\s+','-', project_name_pathsafe)
    project_name_pathsafe = project_name_pathsafe.lower()
    return project_name_pathsafe

def create_project(project_name:str) -> None:
    # "Path safe" project_name
    project_name_safe = make_pathsafe(project_name)
    if not os.path.exists(project_name_safe):
        os.mkdir(project_name_safe)
    else:
        raise projectExists(project_name)

    text = f'''name = "{project_name}"
'''
    with open(f'{project_name_safe}/config.toml', 'w') as f:
        f.write(text)

def delete_project(project:str) -> None:
    if not os.path.exists(project):
        raise projectMissing(project)
    elif os.path.exists(project):
        shutil.rmtree(project)