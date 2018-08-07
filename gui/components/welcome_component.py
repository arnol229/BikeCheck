from framework.gzframe_component import GZFrameComponent
from framework.gzframe_elements import GZFrameButton, GZFrameText, GZFrameContainer, GZFramePicture
from interfaces import face


class WelcomeComponent(GZFrameComponent):
    def __init__(self, element_name, state={}, element_props={}):
        super().__init__(element_name, state=state, element_props=element_props)

    def on_init(self):
        self.reset_history()

    def recognize_face(self):
        self.gzframe.element_by_name('enter_button').disable()
        # self.gzframe.element_by_name('welcome').repeat(500, self.on_face_recognition)
        face = Face()

        face.grab_frame()

        user_detected, user = face.detect_users()

        if user_detected:
            face.draw_user(user)

            self.render(PictureElement(face.face))

            # self.gzframe.element_by_name('welcome').cancel(self.on_face_recognition)
            self.go_to_route('enter_one_more')

        elif face_recognized is False:
            self.gzframe.element_by_name('welcome').cancel(self.on_face_recognition)
            self.go_to_route('enter_both_rfid_and_pin')

    def render(self, props, state):
        return [
            GZFrameText(element_name="header_text", element_props={"text":"Welcome to BikeCheck", "size":40, "font":"Times New Roman", "color":"lightblue"}),
            GZFrameButton(element_name="enter_button", element_props={"text":"Enter", "command": self.recognize_face}),
        ]
