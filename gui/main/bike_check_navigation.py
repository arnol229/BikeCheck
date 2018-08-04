class BikeCheckNavigation:
    def __init__(self, core, views_config, root_view_name):
        self.core = core
        self.back_button = self.core.create('push_button', command=self.on_back, text="Back", enabled=False)
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
