from guizero import Text, TextBox, PushButton, Slider, Picture, Box
from framework.gzframe_ui import GZFrameUI

class GZFrameCore:
    gui_classes = [Text, TextBox, PushButton, Slider, Picture, Box]

    def __init__(self, gzframe, views_config, root_view_name):
        self.gzframe = gzframe
        self.history = []
        self.views = self.create_views(views_config)
        self.root_view_config = self.get_view_config(root_view_name)
        self.current_view_name = None
        self.current_view = None

    def initialize(self):
        self.current_view_name = self.root_view_config['name']
        self.current_view = self.root_view_config['view'](self.gzframe)

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

    def is_history_empty(self):
        return len(self.history) == 0

    def clear_history(self):
        self.history = []
    
    def on_back(self):
        if (len(self.history) > 0):
            last_view_name = self.history.pop()
            last_view_config = self.get_view_config(last_view_name, self.root_view_config)
            self.update_current_view(last_view_config)

    def go_to_view(self, next_view_name):
        next_view_config = self.get_view_config(next_view_name, self.root_view_config)
        self.history.append(self.current_view_name)
        self.update_current_view(next_view_config)

    def update_current_view(self, view_config):
        self.destroy_current_view()
        self.current_view_name = view_config['name']
        self.current_view = view_config['view'](self.gzframe)

    def destroy_current_view(self):
        for element_name in self.current_view.ui.elements:
            for g_class in self.gui_classes:
                element_class = self.current_view.ui.elements[element_name]
                element = getattr(element_class, 'element')
                if isinstance(element, g_class):
                    element.destroy()

    def without_keys(self, d, keys):
        return {x: d[x] for x in d if x not in keys}
