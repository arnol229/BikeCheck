class WelcomeView:
    def __init__(self, core):
        self.core = core
        self.header_text = self.core.create('text', text="Welcome to BikeCheck", size=40, font="Times New Roman", color="lightblue", grid=[])
        self.button = self.core.create('push_button', command=self.on_face_recognition, text="Enter")

    def on_face_recognition(self):
        self.button.disable()
        self.core.app.repeat(500, self.on_exit_view)

    def on_exit_view(self):
        face_recognized = True
        if face_recognized is True:
            self.core.app.cancel(self.on_exit_view)
            self.core.nav.go_to_view('enter_pin')
        elif face_recognized is False:
            self.core.app.cancel(self.on_exit_view)
            self.core.nav.go_to_view('no_recognition')