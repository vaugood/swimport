from nicegui import ui
import welcome

ui.link('Create', welcome.project_maker)
ui.link('Open', welcome.project_opener)
ui.link('Manage', welcome.project_manager)

ui.run()
