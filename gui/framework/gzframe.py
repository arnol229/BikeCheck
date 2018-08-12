from guizero import App
from framework.gzframe_navigation import GZFrameNavigation
from framework.gzframe_renderer import GZFrameRenderer
from framework.gzframe_state import GZFrameState
from framework.gzframe_virtual_view import GZFrameVirtualView

class GZFrame:
    def __init__(self, app_config, routes, state={}):
        self.app = App(**app_config)
        self.app_config = app_config
        self.state = GZFrameState(state)
        self.view = GZFrameRenderer(self, self.state)
        self.nav = GZFrameNavigation(self.app, routes, self.view, self.state)
        #self.change_detector = GZFrameVirtualView(self.app, self.nav, self.view)
        self.view.render(self.view.current_component_tree)

    def set_state(self, state={}):
        self.state.update_state(state)
        #self.change_detector.update_view_on_state_change()

    def get_state(self, name):
        return self.state

    def element_by_name(self, name):
        return self.view.element_by_name(name)

    def on_back(self):
        self.nav.on_back()

    def run(self):
        self.app.display()