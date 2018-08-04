from guizero import Text, TextBox, PushButton, Slider, Picture
from main.bike_check_navigation import BikeCheckNavigation

class BikeCheckCore:
    gui_classes = [Text, TextBox, PushButton, Slider, Picture]
    def __init__(self, app, views_config, root_view_name):
        self.app = app
        self.views_config = views_config
        self.nav = BikeCheckNavigation(self, self.views_config, root_view_name)
        self.current_view_name = self.nav.root_view_config['name']
        self.current_view = self.nav.root_view_config['view'](self)

    def create(self, element, *args, **kwargs):
        if element == 'text':
            return Text(self.app, *args, **kwargs)
        elif element == 'push_button':
            return PushButton(self.app, *args, **kwargs)
        elif element == 'text_box':
            return TextBox(self.app, *args, **kwargs)
        else:
            return None

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
