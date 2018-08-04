from guizero import App, Text, TextBox, PushButton, Slider, Picture

class WelcomeView:
    view_name = 'welcome_view'

    def __init__(self, application, on_exit_view = None):
        self.app = application
        self.on_exit_view = on_exit_view
        self.header_text = Text(self.app, text="Welcome to BikeCheck", size=40, font="Times New Roman", color="lightblue", grid=[])
        self.button = PushButton(self.app, command=self.on_face_recognition, text="Enter")

    def on_face_recognition(self):
        self.button.disable()
        self.app.repeat(500, self.exit_welcome_view)

    def exit_welcome_view(self):
        face_recognized = True
        if face_recognized is True:
            self.app.cancel(self.exit_welcome_view)
            self.on_exit_view(PinView)
        elif face_recognized is False:
            self.app.cancel(self.exit_welcome_view)
            self.on_exit_view(CantRecognizeView)

    def destroy(self):
        self.header_text.destroy()
        self.button.destroy()

class PinView:
    view_name = 'pin_view'

    def __init__(self, application, on_exit_view = None):
        self.app = application
        self.header_text = Text(self.app, text="Welcome PERSON", size=40, font="Times New Roman", color="lightblue", grid=[])
        self.pin_text = Text(self.app, text="Enter your PIN to validate", size=30, font="Times New Roman", color="lightblue", grid=[])
        self.pin_input = TextBox(self.app, command=self.check_pin)
        self.pin_error = Text(self.app, text="", visible=False, color="red")
    
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

    def __init__(self, application, on_exit_view = None):
        self.app = application
        self.header_text = Text(self.app, text="Can't Recognize You!", size=40, font="Times New Roman", color="lightblue", grid=[])

    def destroy(self):
        self.header_text.destroy()

class Navigation:
    views = { 'welcome_view': WelcomeView, 'pin_view': PinView, 'cant_recognize_view': CantRecognizeView }
    def __init__(self, app, initial_view):
        self.app = app
        self.back_button = PushButton(self.app, command=self.on_back, text="Back", enabled=False)
        self.history = []
        self.current_view = initial_view(self.app, self.on_exit_view)

    def on_back(self):
        if (len(self.history) > 0):
            last_view = self.history.pop()
            self.update_current_view(self.views[last_view](self.app, self.on_exit_view), True)
            if (len(self.history) == 0):
                self.back_button.disable()

    def on_exit_view(self, next_view):
        self.update_current_view(next_view(self.app, self.on_exit_view))

    def update_current_view(self, next_view, isBack = False):
        if isBack is False:
            self.history.append(self.current_view.view_name)
        self.current_view.destroy()
        self.current_view = next_view
        self.back_button.enable()

class BikeCheckApp:
    def __init__(self, app):
        self.app = app(title="BikeCheck")
        self.nav = Navigation(app=self.app, initial_view=WelcomeView)

    def start(self):
        self.app.display()

app = BikeCheckApp(App)
app.start()

