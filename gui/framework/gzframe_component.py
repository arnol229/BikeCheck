from framework.gzframe_elements import GZFrameElement, GZFrameElement

class GZFrameComponent(GZFrameElement):
    def __init__(self, element_name, gzframe = None, props={}, state={}, element_props={}, parent_name = None, element = None, index=0):
        super().__init__(element_name=element_name, element_type="component", element_props=element_props, parent_name=parent_name, element=element, index=index)
        self.gzframe = gzframe
        self.props = props
        self.state = state if type(state) is not dict else type('BaseState', (), state)
        self.children = self.render(props=self.props, state=self.state)

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

    def render(self, props, state):
        return []