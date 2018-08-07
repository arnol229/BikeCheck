from guizero import App
from framework.gzframe_navigation import GZFrameNavigation
from framework.gzframe_renderer import GZFrameRenderer
from framework.gzframe_state import GZFrameState
from framework.gzframe_change_detector import GZFrameChangeDetector

class GZFrame:
    def __init__(self, app_config, routes, state={}):
        self.app = App(**app_config)
        self.state = GZFrameState(state)
        self.view = GZFrameRenderer(self)
        self.nav = GZFrameNavigation(self.app, routes, self.view, self.state)
        self.change_detector = GZFrameChangeDetector(self.app, self.view, self.state)
        self.view.render(self.nav.root_component, self.app)

    def element(self, name):
        return self.view.element(name)

    def on_back(self):
        self.nav.on_back()

    def run(self):
        self.app.display()