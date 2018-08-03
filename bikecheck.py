from guizero import App, Text, TextBox, PushButton, Slider, Picture

class WelcomeView:
    def __init__(self, application, on_enter):
        self.app = application
        self.header_text = None
        self.button = None
        self.on_enter = on_enter

    def on_face_recognition(self):
        self.button.disable()
        self.app.repeat(500, self.on_enter)

    def create(self):
        self.header_text = Text(self.app, text="Welcome to BikeCheck", size=40, font="Times New Roman", color="lightblue", grid=[])
        self.button = PushButton(self.app, command=self.on_face_recognition, text="Enter")

    def destroy(self):
        self.header_text.destroy()
        self.button.destroy()

class PinView:
    def __init__(self, application):
        self.app = application
        self.header_text = None
        self.pin_text = None
        self.pin_input = None
        self.pin_error = None
    
    def check_pin(self, enteredKey):
        currentPinEntry = self.pin_input.value + enteredKey

        if (len(currentPinEntry) < 4):
            self.pin_error.text = "The pin is invalid"
            self.pin_error.visible = True
        else:
            self.pin_error.text = ""
            self.pin_error.visible = False

    def create(self):
        self.header_text = Text(self.app, text="Welcome PERSON", size=40, font="Times New Roman", color="lightblue", grid=[])
        self.pin_text = Text(self.app, text="Enter your PIN to validate", size=30, font="Times New Roman", color="lightblue", grid=[])
        self.pin_input = TextBox(self.app, command=self.check_pin)
        self.pin_error = Text(self.app, text="", visible=False, color="red")

    def destroy(self):
        self.header_text.destroy()
        self.pin_text.destroy()
        self.pin_input.destroy()
        self.pin_error.destroy()

class CantRecognizeView:
    def __init__(self, application):
        self.app = application
        self.header_text = None

    def create(self):
        self.header_text = Text(self.app, text="Can't Recognize You!", size=40, font="Times New Roman", color="lightblue", grid=[])

    def destroy(self):
        self.header_text.destroy()

class BikeCheckApp:
    def __init__(self, application):
        self.app = application
        self.welcome_view = WelcomeView(self.app, self.exit_welcome_view)
        self.pin_view = PinView(self.app)
        self.cant_recognize_view = CantRecognizeView(self.app)

    def exit_welcome_view(self):
        face_recognized = True
        if face_recognized is True:
            self.app.cancel(self.exit_welcome_view)
            self.welcome_view.destroy()
            self.pin_view.create()
        elif face_recognized is False:
            self.app.cancel(self.exit_welcome_view)
            self.welcome_view.destroy()
            self.cant_recognize_view.create()

    def start_app(self):
        self.welcome_view.create()
        self.app.display()

instance = BikeCheckApp(App(title="BikeCheck"))

instance.start_app()

