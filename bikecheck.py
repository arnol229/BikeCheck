from guizero import App, Text, TextBox, PushButton, Slider, Picture

class WelcomeView:
    view_name = 'welcome_view'

    def __init__(self, core):
        self.core = core
        self.header_text = Text(self.core.app, text="Welcome to BikeCheck", size=40, font="Times New Roman", color="lightblue", grid=[])
        self.button = PushButton(self.core.app, command=self.on_face_recognition, text="Enter")

    def on_face_recognition(self):
        self.button.disable()
        self.core.app.repeat(500, self.on_exit_view)

    def on_exit_view(self):
        face_recognized = True
        if face_recognized is True:
            self.core.app.cancel(self.on_exit_view)
            self.core.nav.go_to_view('pin')
        elif face_recognized is False:
            self.core.app.cancel(self.on_exit_view)
            self.core.nav.go_to_view('cant_recognize')

class PinView:
    view_name = 'pin_view'

    def __init__(self, core):
        self.core = core
        self.header_text = Text(self.core.app, text="Welcome PERSON", size=40, font="Times New Roman", color="lightblue", grid=[])
        self.pin_text = Text(self.core.app, text="Enter your PIN to validate", size=30, font="Times New Roman", color="lightblue", grid=[])
        self.pin_input = TextBox(self.core.app, command=self.check_pin)
        self.pin_error = Text(self.core.app, text="", visible=False, color="red")
    
    def check_pin(self, enteredKey):
        currentPinEntry = self.pin_input.value + enteredKey

        if (len(currentPinEntry) < 4):
            self.pin_error.text = "The pin is invalid"
            self.pin_error.visible = True
        else:
            self.pin_error.text = ""
            self.pin_error.visible = False

class CantRecognizeView:
    view_name = 'cant_recognize_view'

    def __init__(self, core):
        self.core = core
        self.header_text = Text(self.core.app, text="Can't Recognize You!", size=40, font="Times New Roman", color="lightblue", grid=[])

class Navigation:
    def __init__(self, core, views_config, root_view_name):
        self.core = core
        self.back_button = PushButton(self.core.app, command=self.on_back, text="Back", enabled=False)
        self.history = []
        self.views = self.create_views(views_config)
        self.root_view_config = self.get_view_config(root_view_name)

    def create_views(self, views_config):
        result = []
        for key, value in views_config.items():
            result.append({'name': key, 'view': value})
        return result
    
    def get_view_config(self, view_name, default = None):
        view_config = next(
            (view for view in self.views if view['name'] == view_name), default
            )
        return view_config
    
    def on_back(self):
        if (len(self.history) > 0):
            last_view_name = self.history.pop()
            last_view = self.get_view_config(last_view_name, self.root_view_config)
            self.core.update_current_view(last_view)
            if (len(self.history) == 0):
                self.back_button.disable()

    def go_to_view(self, next_view_name):
        next_view = self.get_view_config(next_view_name, self.root_view_config)
        self.history.append(self.core.current_view_name)
        self.core.update_current_view(next_view)
        self.back_button.enable()


class Core:
    gui_classes = [Text, TextBox, PushButton, Slider, Picture]
    def __init__(self, app, root_view_name, views_config):
        self.app = app
        self.views_config = views_config
        self.nav = Navigation(self, self.views_config, root_view_name)
        self.current_view_name = self.nav.root_view_config['name']
        self.current_view = self.nav.root_view_config['view'](self)

    def update_current_view(self, view_config):
        self.destroy_current_view()
        self.current_view_name = view_config['name']
        self.current_view = view_config['view'](self)

    def destroy_current_view(self):
        view_attrs = self.current_view.__dict__
        for attr in view_attrs:
            for g_class in self.gui_classes:
                class_attr = getattr(self.current_view, attr)
                if isinstance(class_attr, g_class):
                    class_attr.destroy()

class BikeCheckApp:
    def __init__(self, app, views_config):
        self.app = app(title="BikeCheck")
        self.core = Core(app=self.app, root_view_name='welcome', views_config=views_config)

    def start(self):
        self.app.display()

views_config = {
    'welcome': WelcomeView,
    'pin': PinView,
    'cant_recognize': CantRecognizeView
}
app = BikeCheckApp(App, views_config)
app.start()

