from framework.gzframe_view import GZFrameView

class WelcomeView(GZFrameView):
    def __init__(self, gzframe):
        super().__init__(gzframe)
        self.reset_history()
        self.ui.render_text(element_name="helper_text", text="Welcome to BikeCheck", size=40, font="Times New Roman", color="lightblue", grid=[])
        self.ui.render_button(element_name="enter_button", command=self.on_face_recognition, text="Enter")

    def on_face_recognition(self):
        self.ui.element('enter_button').disable()
        self.ui.element('root').repeat(500, self.on_exit_view)

    def on_exit_view(self):
        face_recognized = True
        if face_recognized is True:
            self.ui.element('root').cancel(self.on_exit_view)
            self.go_to_view('enter_pin')
        elif face_recognized is False:
            self.ui.element('root').cancel(self.on_exit_view)
            self.go_to_view('no_recognition')