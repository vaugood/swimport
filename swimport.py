import os
import shutil
import re

class noName(Exception):
    'Raised when no project name is specified.'
    def __init__(self) -> None:
        msg = 'Name is required'
        super().__init__(msg)

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

def make_project_name(project_name:str) -> str:
    project_name_pathsafe = project_name.strip()
    project_name_pathsafe = re.sub(r'[^a-zA-Z0-9_. -]', '', project_name_pathsafe)
    project_name_pathsafe = re.sub(r'\s+','-', project_name_pathsafe)
    project_name_pathsafe = project_name_pathsafe.lower()
    project_name_pathsafe = project_name_pathsafe+'.swim'
    return project_name_pathsafe

def create_project(project_name:str) -> None:
    # "Path safe" project_name
    project_name_safe = make_project_name(project_name)
    if not project_name:
        raise noName

    if not os.path.exists(project_name_safe):
        os.mkdir(project_name_safe)
    else:
        raise projectExists(project_name)

    text = f'''title = "{project_name}"
'''
    with open(f'{project_name_safe}/config.toml', 'w') as f:
        f.write(text)

def delete_project(project:str) -> None:
    if not os.path.exists(project):
        raise projectMissing(project)
    elif os.path.exists(project):
        shutil.rmtree(project)

def list_projects() -> list[dict]:
    # TODO: When project_directory argument is given, search that directory
    # for project files instead of the local directory.
    return [{'name':i} for i in os.listdir(os.curdir) if i[-5:] == '.swim']