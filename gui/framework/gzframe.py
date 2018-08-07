from guizero import App
from framework.gzframe_navigation import GZFrameNavigation
from framework.gzframe_renderer import GZFrameRenderer

class GZFrame:
    def __init__(self, app_config, routes, state=None):
        self.app = App(**app_config)
        self.state = state
        self.current_view = GZFrameRenderer(self)
        self.nav = GZFrameNavigation(self.app, routes, self.current_view, self.state)
        self.current_view.render(self.nav.root_component, self.app)

    def element(self, name):
        elements = getattr(self.current_view, 'elements')
        return getattr(elements[name], 'element')

    def on_back(self):
        self.nav.on_back()

    def run(self):
        self.app.display()