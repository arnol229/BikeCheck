from framework.gzframe_ui import GZFrameUI

class GZFrameView:
    def __init__(self, gzframe):
        self.gzframe = gzframe
        self.state = self.gzframe.state
        self.ui = GZFrameUI(self.gzframe)
    
    def go_to_view(self, view):
        self.gzframe.core.go_to_view(view)

    def on_back(self):
        self.gzframe.core.on_back()

    def reset_history(self):
        self.gzframe.core.clear_history()

    def is_history_empty(self):
        return not self.gzframe.core.is_history_empty()