from nicegui import ui
import xml.etree.ElementTree as ET

@ui.page('/swimview')
def lanespage(project_name:str):
    ui.link('Back','/')
    ui.label(f'{project_name}')
    lanes_xml = ET.parse(f'{project_name}/lanes.xml').getroot()
    for swimlane in lanes_xml:
        with ui.row():
            ui.label(swimlane.find('name').text)
            with ui.scroll_area().classes('w-64 h-32 border'):
                lapview(swimlane)

def lapview(swimlane):
    match swimlane.get('type'):
        case 'pandas':
            for lap in swimlane.find('swimlaps').findall('operation'):
                ui.label(lap.text)
        case 'script ':
            ui.label(swimlane.find('name').text)