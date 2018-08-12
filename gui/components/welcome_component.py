from framework.gzframe_component import GZFrameComponent
from framework.gzframe_elements import GZFrameButton, GZFrameText, GZFrameContainer, GZFramePicture
from interfaces.face import Face
from PIL import Image

import time

class WelcomeComponent(GZFrameComponent):
    def __init__(self, element_name, state={}, props={}):
        super().__init__(element_name, state=state, props=props)

    def gz_on_init(self):
        self.reset_history()

    def on_frame(self):
        if (self.state.face.frame is not None):
            self.element.cancel(self.on_frame)
            user_detected, user = self.state.face.detect_users()
            if type(user) == list:
                user = user[0]

            if user_detected:
                cropped_user_img = self.state.face.find_user(user)
                im = Image.fromarray(cropped_user_img)
                self.state.update_state({'auth': {'face_id': user.get('faceId')}})
                pic = GZFramePicture(element_name="user_picture", props={'image': im})
                text = GZFrameText(element_name="picture_text", props={"text":"Welcome {}!".format(user.get('name', 'Associate')), "size":50, "font":"Times New Roman", "color":"black"})
                self.gzframe.view.render(text, parent=self.gzframe.app)
                self.gzframe.view.render(pic, parent=self.gzframe.app)
                # pic.element.show()
            self.gzframe.app.after(4000, self.go_to_verify)

    def recognize_face(self):
        self.gzframe.element_by_name('enter_button').disable()
        if not isinstance(self.state.face, Face):
            self.state.face = Face()
        self.state.face.grab_frame()
        self.element.repeat(200, self.on_frame)
        

    def go_to_verify(self):
        self.go_to_route('verify')

    def render(self, state):
        return [
            GZFrameText(element_name="header_text", props={"text":"Welcome to BikeCheck", "size":40, "font":"Times New Roman", "color":"lightblue"}),
            GZFrameButton(element_name="enter_button", props={"text":"Enter", "command": self.recognize_face}),
        ]
