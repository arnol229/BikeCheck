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
        if (self.face.frame is not None):
            self.element.cancel(self.on_frame)
            user_detected, user = self.face.detect_users()
            if type(user) == list:
                user = user[0]

            if user_detected:
                cropped_user_img = self.face.find_user(user)
                im = Image.fromarray(cropped_user_img)
                self.state.update_state({'auth': {'face': im}})
                pic = GZFramePicture(element_name="user_picture", element_props={'image': self.state.auth['face']})
                text = GZFrameText(element_name="picture_text", element_props={"text":"Welcome {}!".format(user.get('name', 'Associate')), "size":50, "font":"Times New Roman", "color":"black"})
                self.gzframe.view.render(text, parent=self.gzframe.app)
                self.gzframe.view.render(pic, parent=self.gzframe.app)
                # pic.element.show()
            self.gzframe.app.after(4000, self.go_to_verify)

    def recognize_face(self):
        self.gzframe.element_by_name('enter_button').disable()
        # self.gzframe.element_by_name('welcome').repeat(500, self.on_face_recognition)
        self.face = Face()
        self.face.grab_frame()
        self.element.repeat(200, self.on_frame)
        

    def go_to_verify(self):
        self.go_to_route('verify')

    def render(self, state):
        return [
<<<<<<< HEAD
            GZFrameText(element_name="header_text", element_props={"text":"Welcome to BikeCheck", "size":40, "font":"Times New Roman", "color":"lightblue"}),
            GZFrameButton(element_name="enter_button", element_props={"text":"Enter", "command": self.recognize_face}),
        ]
=======
            GZFrameText(element_name="header_text", props={"text":"Welcome to BikeCheck", "size":40, "font":"Times New Roman", "color":"lightblue"}),
            GZFrameButton(element_name="enter_button", props={"text":"Enter", "command": self.recognize_face}),
        ]
>>>>>>> ccff6c9e727d955c6e01c7d97b4e9a682568c665
