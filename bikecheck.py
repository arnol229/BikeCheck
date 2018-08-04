from guizero import App, Text, TextBox, PushButton, Slider, Picture

class WelcomeView:
    view_name = 'welcome_view'

    def __init__(self, application, on_enter, history):
        self.app = application
        self.on_enter = on_enter
        self.header_text = Text(self.app, text="Welcome to BikeCheck", size=40, font="Times New Roman", color="lightblue", grid=[])
        self.button = PushButton(self.app, command=self.on_face_recognition, text="Enter")
        self.history = history

    def on_face_recognition(self):
        self.button.disable()
        self.app.repeat(500, self.on_enter)

    def destroy(self):
        self.header_text.destroy()
        self.button.destroy()

class PinView:
    view_name = 'pin_view'

    def __init__(self, application, history):
        self.app = application
        self.header_text = Text(self.app, text="Welcome PERSON", size=40, font="Times New Roman", color="lightblue", grid=[])
        self.pin_text = Text(self.app, text="Enter your PIN to validate", size=30, font="Times New Roman", color="lightblue", grid=[])
        self.pin_input = TextBox(self.app, command=self.check_pin)
        self.pin_error = Text(self.app, text="", visible=False, color="red")
        self.history = history
    
    def check_pin(self, enteredKey):
        currentPinEntry = self.pin_input.value + enteredKey

        if (len(currentPinEntry) < 4):
            self.pin_error.text = "The pin is invalid"
            self.pin_error.visible = True
        else:
            self.pin_error.text = ""
            self.pin_error.visible = False

    def destroy(self):
        self.header_text.destroy()
        self.pin_text.destroy()
        self.pin_input.destroy()
        self.pin_error.destroy()

class CantRecognizeView:
    view_name = 'cant_recognize_view'

    def __init__(self, application, history):
        self.app = application
        self.header_text = Text(self.app, text="Can't Recognize You!", size=40, font="Times New Roman", color="lightblue", grid=[])
        self.history = history

    def destroy(self):
        self.header_text.destroy()

class BikeCheckApp:
    def __init__(self, app, history):
        self.app = app(title="BikeCheck")
        self.back_button = PushButton(self.app, command=self.on_back, text="Back")
        self.current_view = WelcomeView(self.app, self.exit_welcome_view, history)
        self.history = history

    def on_back(self):
        if (len(self.history) > 1):
            last_view = self.history.pop()
            if (last_view == CantRecognizeView.view_name):
                self.current_view.destroy()
                self.current_view = CantRecognizeView(self.app, self.history)
            if (last_view == PinView.view_name):
                self.current_view.destroy()
                self.current_view = PinView(self.app, self.history)
        elif(len(self.history) == 1):
            self.current_view.destroy()
            self.current_view = WelcomeView(self.app, self.exit_welcome_view, self.history)

    def exit_welcome_view(self):
        face_recognized = True
        if face_recognized is True:
            self.app.cancel(self.exit_welcome_view)
            self.current_view.destroy()
            self.current_view = PinView(self.app, self.history)
        elif face_recognized is False:
            self.app.cancel(self.exit_welcome_view)
            self.current_view.destroy()
            self.current_view = CantRecognizeView(self.app, self.history)

    def start(self):
        self.app.display()

history = ['welcome_view']
app = BikeCheckApp(App, history)
app.start()

