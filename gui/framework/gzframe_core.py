from guizero import Box
from framework.gzframe_ui import GZFrameUI

class GZFrameCore:
    def __init__(self, gzframe, views_config, root_view_name):
        self.gzframe = gzframe
        self.ui = GZFrameUI(self.gzframe)
        self.back_button = self.ui.render_button(command=self.on_back, text="Back", enabled=False)
        self.history = []
        self.views = self.create_views(views_config)
        self.root_view_config = self.get_view_config(root_view_name)
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

    def reset_history(self):
        self.history = []
        self.back_button.disable()
    
    def on_back(self):
        if (len(self.history) > 0):
            last_view_name = self.history.pop()
            last_view_config = self.get_view_config(last_view_name, self.root_view_config)
            self.update_current_view(last_view_config)
            if (len(self.history) == 0):
                self.back_button.disable()

    def go_to_view(self, next_view_name):
        next_view_config = self.get_view_config(next_view_name, self.root_view_config)
        self.history.append(self.current_view_name)
        self.update_current_view(next_view_config)
        self.back_button.enable()

    def update_current_view(self, view_config):
        self.destroy_current_view()
        self.current_view_name = view_config['name']
        self.current_view = view_config['view'](self.gzframe)

    def destroy_current_view(self):
        view_attrs = self.current_view.__dict__
        for attr in view_attrs:
            for g_class in self.ui.gui_classes:
                class_attr = getattr(self.current_view, attr)
                if isinstance(class_attr, g_class):
                    class_attr.destroy()
        if isinstance(self.current_view.ui.container, Box):
            self.current_view.ui.container.destroy()
