from framework.gzframe_component import GZFrameComponent
from framework.gzframe_elements import GZFrameButton, GZFrameText, GZFrameContainer

class WelcomeComponent(GZFrameComponent):
    def __init__(self, element_name, props={}, state={}, element_props={}):
        super().__init__(element_name, props=props, state=state, element_props=element_props)

    def on_init(self):
        self.reset_history()

    def recognize_face(self):
        self.gzframe.element('enter_button').disable()
        self.gzframe.element('welcome').repeat(500, self.on_face_recognition)

    def on_face_recognition(self):
        face_recognized = True
        if face_recognized is True:
            self.gzframe.element('welcome').cancel(self.on_face_recognition)
            self.go_to_route('enter_pin')
        elif face_recognized is False:
            self.gzframe.element('welcome').cancel(self.on_face_recognition)
            self.go_to_route('no_recognition')

    def render(self, props, state):
        return [
            GZFrameText(element_name="header_text", element_props={"text":"Welcome to BikeCheck", "size":40, "font":"Times New Roman", "color":"lightblue"}),
            GZFrameButton(element_name="enter_button", element_props={"text":"Enter", "command": self.recognize_face}),
        ]