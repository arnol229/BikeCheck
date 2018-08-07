from framework.gzframe_elements import GZFrameElement, GZFrameElement

class GZFrameComponent(GZFrameElement):
    def __init__(self, element_name, gzframe = None, state={}, props={}, parent_name = None, element = None, index=0):
        super().__init__(element_name=element_name, element_type="component", props=props, parent_name=parent_name, element=element, index=index)
        self.gzframe = gzframe
        self.state = state
        self.children = self.render(state)

    def gz_on_init(self):
        pass

    def gz_on_change(self):
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