from guizero import App
from framework.gzframe_core import GZFrameCore

class GZFrame:
    def __init__(self, app_config, routes, state=None):
        self.app = App(**app_config)
        self.state = state
        self.core = GZFrameCore(self, routes)
        self.core.update_current_view(self.core.root_route)

    def element(self, name):
        current_view = getattr(self.core, 'current_view')
        elements = getattr(current_view, 'elements')
        return getattr(elements[name], 'element')

    def run(self):
        self.app.display()