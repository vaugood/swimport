from nicegui import ui
import swimport as sp

pj_name = ui.input(label='Project Name',
                   on_change=lambda e: safename_preview.set_text('Project Folder: ' + sp.make_pathsafe(e.value)),
                   validation={'Input too long!': lambda value: len(value) < 200})

safename_preview = ui.label()

ui.button('Create', on_click=lambda: sp.create_project(pj_name.value))

ui.run()
