from framework.gzframe_component import GZFrameComponent
from framework.gzframe_elements import GZFrameButton, GZFrameText, GZFrameContainer, GZFramePicture
from interfaces.face import Face
from PIL import Image

import time

class WelcomeComponent(GZFrameComponent):
    def __init__(self, element_name, state={}, props={}):
        super().__init__(element_name, state=state, props=props, width=800)
        self.user_detected = None
        self.user = None
        self.retries = 0

    def gz_on_init(self):
        self.reset_history()


    def on_frame(self):
        if (self.state.face.frame is not None):
            self.user_detected, self.user = self.state.face.detect_users()
            self.element.cancel(self.on_frame)
            self.element.repeat(2000, self.on_user_detected)

    def on_user_detected(self):
        if self.user_detected is not None:
            self.element.cancel(self.on_user_detected)
            if type(self.user) == list and len(self.user) > 0:
                user = self.user[0]
                cropped_user_img = self.state.face.find_user(user)
                im = Image.fromarray(cropped_user_img)
                self.state.update_state({'auth': {'face': im}})
                pic = GZFramePicture(element_name="user_picture", props={'image': self.state.auth['face']}, height=200, width=200)
                text = GZFrameText(element_name="picture_text", props={"text":"Welcome {}!".format(user.get('name', 'Associate')), "size":50, "font":"Times New Roman", "color":"black"})
                self.gzframe.view.destroy('welcome_group')
                self.gzframe.view.render(text)
                self.gzframe.view.render(pic)
                # pic.element.show()
                self.gzframe.app.after(2000, self.go_to_verify)
            else:
                self.user_detected = None
                self.retries += 1
                self.recognize_face()

    def recognize_face(self):
        print(self.retries)
        if self.retries < 5:
            self.gzframe.element_by_name('enter_button').disable()
            if not isinstance(self.state.face, Face):
                self.state.face = Face()
            self.state.face.grab_frame()
            self.element.repeat(500, self.on_frame)
        else:
            self.retries = 0
            self.gzframe.element_by_name('enter_button').enable()
        

    def go_to_verify(self):
        self.go_to_route('verify')

    def render(self, state):
        return [
            GZFrameContainer(element_name='welcome_group', children=[
                GZFrameText(element_name="header_text", props={"text":"Welcome to BikeCheck", "size":40, "font":"Times New Roman", "color":"lightblue"}),
                GZFrameButton(element_name="enter_button", props={"text":"Enter", "command": self.recognize_face}),
            ])
        ]
