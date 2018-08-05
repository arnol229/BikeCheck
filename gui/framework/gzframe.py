from guizero import App
from framework.gzframe_core import GZFrameCore

class GZFrame:
    def __init__(self, app_config, views_config, root_view_name, state=None):
        self.app = App(**app_config)
        self.state = state
        self.core = GZFrameCore(self, views_config, root_view_name)
        self.core.initialize()

    def run(self):
        self.app.display()