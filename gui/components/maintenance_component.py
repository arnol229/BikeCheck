from framework.gzframe_component import GZFrameComponent
from framework.gzframe_elements import GZFrameButton, GZFrameText, GZFrameContainer

class MaintenanceComponent(GZFrameComponent):
    def __init__(self, element_name, state={}, element_props={}):
        super().__init__(element_name, state=state, element_props=element_props)

    def render(self, props, state):
        return [
            GZFrameContainer(element_name='app_controls_group', children=[
                GZFrameButton(element_name='back_button', element_props={'command': self.on_back, 'text': 'Back'}),
            ]),
            GZFrameText(element_name="header_text", element_props={"text":"Maintenance", "size":40, "font":"Times New Roman", "color":"lightblue"}),
        ]