from guizero import App
from framework.gzframe_core import GZFrameCore

class GZFrame:
    def __init__(self, title, views_config, root_view_name, state=None):
        self.app = App(title=title)
        self.state = state
        self.core = GZFrameCore(self, views_config, root_view_name)

    def run(self):
        self.app.display()