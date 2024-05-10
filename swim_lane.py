import swim_operations
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


def swim(project_name:str) -> pd.DataFrame:
    'Now with custom properties!'
    tree = ET.parse(f'''{project_name}/lanes.xml''')
    swimlanes = tree.getroot().findall('swimlane')
    for swimlane in swimlanes:
        data = pd.read_csv(f'''{project_name}/{swimlane.find('input').text}''')
        data.attrs['lane'] = swimlane.find('lane').text
        for swimlap in swimlane.findall('swimlap'):
            data = swim_operations.operate(data, swimlap)
        return data

# The only data type supported right now is tabular data as pd.DataFrame
# TODO: Figure out the best way to load in non-tabular data - see products.py for an idea
def swimx(project_name:str):
    tree = ET.parse(f'''{project_name}/lanes.xml''')
    swimlanes = tree.getroot().findall('swimlane')
    for swimlane in swimlanes:
        data = pd.read_csv(f'''{project_name}/{swimlane.find('input').text}''')
        for swimlap in swimlane.findall('swimlap'):
            data = swim_operations.operate(data, swimlap)
    return data