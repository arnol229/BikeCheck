from framework.gzframe_controller import GZFrameController
from framework.gzframe_element import GZFrameButton, GZFrameText, GZFrameContainer

class WelcomeCtrl(GZFrameController):
    def __init__(self, gzframe):
        super().__init__(gzframe)

    def on_init(self):
        self.reset_history()

    def recognize_face(self):
        self.view.element('enter_button').disable()
        self.view.element('root').repeat(500, self.on_face_recognition)

    def on_face_recognition(self):
        face_recognized = True
        if face_recognized is True:
            self.view.element('root').cancel(self.on_face_recognition)
            self.go_to_route('enter_pin')
        elif face_recognized is False:
            self.view.element('root').cancel(self.on_face_recognition)
            self.go_to_route('no_recognition')

    def render(self, state):
        return [
            GZFrameText(element_name="header_text", element_props={"text":"Welcome to BikeCheck", "size":40, "font":"Times New Roman", "color":"lightblue"}),
            GZFrameButton(element_name="enter_button", element_props={"text":"Enter", "command": self.recognize_face})
        ]