from nicegui import ui
import swimport as sp

def projects_grid() -> ui.aggrid:
    grid = ui.aggrid({
        'columnDefs':[
            {'headerName':'Name','field':'name','checkboxSelection':True}
        ],
        'rowData':sp.list_projects(),
    }).classes('max-h-40')
    return grid

def handle_create(name):
    try:
        sp.create_project(name)
        ui.notify(f'Created {name}')
    except sp.projectExists:
        ui.notify(f'{name} already exists')
    except sp.noName:
        ui.notify('Name is required')

@ui.page('/create')
def project_maker():
    ui.link('Back','/')
    pj_name = ui.input(label='Project Name',
                    on_change=lambda e: safename_preview.set_text('Project will save as: ' + sp.make_project_name(e.value) if e.value else ''),
                    validation={'Input too long!': lambda value: len(value) < 200})
    safename_preview = ui.label()
    ui.button('Create', on_click=lambda: handle_create(pj_name.value))

@ui.page('/open')
def project_opener():
    ui.link('Back','/')
    async def open_selected_project():
        project = await projects_list.get_selected_row()
        if project:
            try:
                ui.notify(f'''Open {project['name']}''')
            except sp.projectMissing:
                ui.notify(f'''{project['name']} has moved, changed, or deleted. Try reloading.''')
        else:
            ui.notify('Select a project to open!')
    projects_list = projects_grid()
    ui.button('Open', on_click=open_selected_project)

@ui.page('/manage')
def project_manager():
    ui.link('Back','/')
    async def delete_selected_project():
        project = await projects_list.get_selected_row()
        if project:
            try:
                sp.delete_project(project['name'])
                ui.navigate.reload()
                # ui.notify(f'''{project['name']} deleted''')
            except sp.projectMissing:
                ui.notify(f'''{project['name']} should be gone already. Try reloading.''')
        else:
            ui.notify('Select a project to delete!')
    projects_list = projects_grid()
    ui.button('Delete', on_click=delete_selected_project)