import importlib.util
import sys
import pandas as pd
import xml.etree.ElementTree as ET
import tomllib

class Project:
    def __init__(self, project_name):
        self.project_name = project_name

class Lane:
    def __init__(self, dataframe:pd.DataFrame, lane_no:int) -> None:
        self.dataframe = dataframe
        self.lane_no = lane_no
        self.orchestration = []

    # This probably wants to be a new class that instantiates as a child of Lane ?
    def new_lap(self, operation):
        lap = {'lane':self.lane_no,'operation':operation}
        self.orchestration.append(lap)

# The only data type supported right now is tabular data as pd.DataFrame
# TODO: Figure out the best way to load in non-tabular data - see products.py for an idea
def swim(project_name:str):
    tree = ET.parse(f'''{project_name}/lanes.xml''')
    swimlanes = tree.getroot().findall('swimlane')
    data = {}
    for swimlane in swimlanes:
        swimlane_name = swimlane.find('name').text

        match swimlane.attrib['type']:
            case 'pandas':
                swimlaps = swimlane.find('swimlaps')
                for lap in swimlaps:
                    exec(lap.text, globals())
                data.update({swimlane_name:globals()[swimlane_name]})
            case 'script':
                args = {}
                for argument in swimlane.find('arguments').findall('argument'):
                    argname = argument.find('argname').text
                    argvalue = argument.find('argvalue').text
                    args.update({argname:argvalue})
                arguments = ','.join([f'{key}={value}' for key, value in args.items()])
                ###
                exec(f'spec = importlib.util.spec_from_file_location("{swimlane_name}_module", "{project_name}/scripts/{swimlane_name}.py")', globals())
                exec(f'foo = importlib.util.module_from_spec(spec)', globals())
                # sys.modules[swimlane_name] = foo
                exec('spec.loader.exec_module(foo)', globals())
                exec(f'{swimlane_name} = foo.main({arguments})', globals())
        data.update({swimlane_name:globals()[swimlane_name]})
    return data
                