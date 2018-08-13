from framework.gzframe_elements import GZFrameContainer

class GZFrameComponent(GZFrameContainer):
    def __init__(self, element_name, gzframe = None, state={}, props={}, parent= None, element = None, width=None, index=0):
        super().__init__(element_name=element_name, props=props, parent=parent, element=element, width=width, index=index)
        self.element_type = "component"
        self.gzframe = gzframe
        self.state = state
        self.children = self.render(state)

    def gz_on_init(self):
        pass

    def gz_on_change(self):
        pass

    def gz_on_destroy(self):
        pass
    
    def go_to_route(self, view):
        self.gzframe.nav.go_to_route(view)

    def on_back(self):
        self.gzframe.nav.on_back()

    def reset_history(self):
        self.gzframe.nav.clear_history()

    def is_history_empty(self):
        return not self.gzframe.nav.is_history_empty()

    def render(self, state):
        return []