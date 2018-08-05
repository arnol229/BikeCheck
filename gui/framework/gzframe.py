from framework.gzframe_state import GZFrameState
from framework.gzframe_core import GZFrameCore
from framework.gzframe_navigation import GZFrameNavigation

class GZFrame:
    def __init__(self, app, views_config, root_view_name):
        self.app = app
        self.state = GZFrameState()
        self.core = GZFrameCore(app=app)
        self.nav = GZFrameNavigation(self, views_config, root_view_name)