from framework.gzframe_ui import GZFrameUI

class GZFrameView:
    def __init__(self, gzframe):
        self.gzframe = gzframe
        self.ui = GZFrameUI(self.gzframe)
    
    def go_to_view(self, view):
        self.gzframe.nav.go_to_view(view)