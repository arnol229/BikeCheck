from guizero import App, Text, TextBox, PushButton, Slider, Picture

class WelcomeView:
    view_name = 'welcome_view'

    def __init__(self, nav):
        self.nav = nav

    def create(self):
        self.header_text = Text(self.nav.app, text="Welcome to BikeCheck", size=40, font="Times New Roman", color="lightblue", grid=[])
        self.button = PushButton(self.nav.app, command=self.on_face_recognition, text="Enter")

    def on_face_recognition(self):
        self.button.disable()
        self.nav.app.repeat(500, self.on_exit_view)

    def on_exit_view(self):
        face_recognized = True
        if face_recognized is True:
            self.nav.app.cancel(self.on_exit_view)
            self.nav.go_to_view('pin_view')
        elif face_recognized is False:
            self.nav.app.cancel(self.on_exit_view)
            self.nav.go_to_view('cant_recognize_view')

    def destroy(self):
        self.header_text.destroy()
        self.button.destroy()

class PinView:
    view_name = 'pin_view'

    def __init__(self, nav):
        self.nav = nav
    
    def create(self):
        self.header_text = Text(self.nav.app, text="Welcome PERSON", size=40, font="Times New Roman", color="lightblue", grid=[])
        self.pin_text = Text(self.nav.app, text="Enter your PIN to validate", size=30, font="Times New Roman", color="lightblue", grid=[])
        self.pin_input = TextBox(self.nav.app, command=self.check_pin)
        self.pin_error = Text(self.nav.app, text="", visible=False, color="red")
    
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

    def __init__(self, nav):
        self.nav = nav

    def create(self):
        self.header_text = Text(self.nav.app, text="Can't Recognize You!", size=40, font="Times New Roman", color="lightblue", grid=[])

    def destroy(self):
        self.header_text.destroy()


class Navigation:
    def __init__(self, app, root_view, views):
        self.app = app
        self.back_button = PushButton(self.app, command=self.on_back, text="Back", enabled=False)
        self.history = []
        self.views = self.create_views(views)
        self.current_view = root_view(self)
        self.current_view.create()

    def create_views(self, views_list):
        views = {}
        for view in views_list:
            views[view.view_name] = view
        return views
    
    def get_view(self, view_name):
        return self.views[view_name]

    def on_back(self):
        if (len(self.history) > 0):
            last_view = self.history.pop()
            self.update_current_view(self.views[last_view], True)
            if (len(self.history) == 0):
                self.back_button.disable()

    def go_to_view(self, next_view_key):
        next_view = self.get_view(next_view_key)
        self.update_current_view(next_view)

    def update_current_view(self, next_view, isBack = False):
        if isBack is False:
            self.history.append(self.current_view.view_name)
        self.current_view.destroy()
        self.current_view = next_view(self)
        self.current_view.create()
        self.back_button.enable()

class BikeCheckApp:
    def __init__(self, app, views):
        self.app = app(title="BikeCheck")
        self.nav = Navigation(app=self.app, root_view=WelcomeView, views=views)

    def start(self):
        self.app.display()

views = [WelcomeView, PinView, CantRecognizeView]
app = BikeCheckApp(App, views)
app.start()

