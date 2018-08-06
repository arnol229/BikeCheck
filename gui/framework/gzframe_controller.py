from framework.gzframe_view import GZFrameView

class GZFrameController:
    def __init__(self, gzframe):
        self.gzframe = gzframe
        self.state = self.gzframe.state
        self.on_init()
        self.template = self.render(self.gzframe.state)
        self.view = GZFrameView(self.gzframe, self.template)

    def on_init(self):
        pass
    
    def go_to_route(self, view):
        self.gzframe.core.go_to_route(view)

    def on_back(self):
        self.gzframe.core.on_back()

    def reset_history(self):
        self.gzframe.core.clear_history()

    def is_history_empty(self):
        return not self.gzframe.core.is_history_empty()

    def render(self, state):
        return []