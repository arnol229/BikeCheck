class BikeCheckNavigation:
    def __init__(self, core, views_config, root_view_name):
        self.core = core
        self.nav_header = self.core.create('box', self.core.app)
        self.back_button = self.core.create('push_button', self.nav_header, command=self.on_back, text="Back", visible=False)
        self.history = []
        self.is_authenticated = False
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

    def reset_history(self):
        self.history = []
        self.back_button.hide()
    
    def on_back(self):
        if (len(self.history) > 0):
            last_view_name = self.history.pop()
            last_view = self.get_view_config(last_view_name, self.root_view_config)
            self.core.update_current_view(last_view)
            if (len(self.history) == 0):
                self.back_button.hide()

    def go_to_view(self, next_view_name, reset_history = False):
        next_view = self.get_view_config(next_view_name, self.root_view_config)
        self.history.append(self.core.current_view_name)
        self.core.update_current_view(next_view)
        if reset_history == False:
            self.back_button.show()
        else:
            self.reset_history()
