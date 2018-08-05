from framework.gzframe_view import GZFrameView

class WelcomeView(GZFrameView):
    def __init__(self, gzframe):
        super().__init__(gzframe)
        self.header_text = self.ui.render_text(text="Welcome to BikeCheck", size=40, font="Times New Roman", color="lightblue", grid=[])
        self.button = self.ui.render_button(command=self.on_face_recognition, text="Enter")

    def on_face_recognition(self):
        self.button.disable()
        self.ui.start_loop(500, self.on_exit_view)

    def on_exit_view(self):
        face_recognized = True
        if face_recognized is True:
            self.ui.cancel_loop(self.on_exit_view)
            self.go_to_view('enter_pin')
        elif face_recognized is False:
            self.ui.cancel_loop(self.on_exit_view)
            self.go_to_view('no_recognition')