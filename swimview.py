from nicegui import ui
import xml.etree.ElementTree as ET

@ui.page('/swimview')
def lanespage(project_name:str):
    ui.link('Back','/')
    ui.label(f'{project_name}')
    lanes_xml = ET.parse(f'{project_name}/lanes.xml').getroot()
    with ui.row():
        for swimlane in lanes_xml:
            ui.label(swimlane.find('name').text)

def laneview():
    ...