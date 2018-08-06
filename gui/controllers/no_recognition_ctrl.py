from framework.gzframe_controller import GZFrameController
from framework.gzframe_element import GZFrameButton, GZFrameText, GZFrameContainer

class NoRecognitionCtrl(GZFrameController):
    def __init__(self, gzframe):
        super().__init__(gzframe)

    def render(self, state):
        return [
            GZFrameContainer(element_name='app_controls_group', children=[
                GZFrameButton(element_name='back_button', element_props={'command': self.on_back, 'text': 'Back'}),
            ]),
            GZFrameText(element_name="header_text", element_props={"text":"Can't Recognize You!", "size":40, "font":"Times New Roman", "color":"lightblue"}),
        ]