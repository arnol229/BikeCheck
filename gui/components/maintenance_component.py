from framework.gzframe_component import GZFrameComponent
from framework.gzframe_elements import GZFrameButton, GZFrameText, GZFrameContainer

class MaintenanceComponent(GZFrameComponent):
    def __init__(self, element_name, state={}, props={}):
        super().__init__(element_name, state=state, props=props)

    def render(self, state):
        return [
            GZFrameContainer(element_name='app_controls_group', children=[
                GZFrameButton(element_name='back_button', props={'command': self.on_back, 'text': 'Back'}),
            ]),
            GZFrameText(element_name="header_text", props={"text":"Maintenance", "size":40, "font":"Times New Roman", "color":"lightblue"}),
        ]