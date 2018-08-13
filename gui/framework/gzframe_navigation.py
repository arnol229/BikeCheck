from framework.gzframe_renderer import GZFrameRenderer

class GZFrameNavigation:

    def __init__(self, app, routes, view, state):
        self.app = app
        self.state = state
        self.history = []
        self.routes = routes
        self.root_route = self.get_root_route(routes)
        self.current_route = self.root_route
        self.current_view = view
        self.update_current_component_tree(self.current_route)

    def get_root_route(self, routes):
        root_route = None
        for route in routes:
            if 'is_root' in route:
                if route['is_root'] is True:
                    root_route = route

        if root_route is None:
            return routes[0]
        else:
            return root_route
    
    def get_route(self, route_name):
        return next(
            (component for component in self.routes if component['name'] == route_name), self.root_route
        )

    def is_history_empty(self):
        return len(self.history) == 0

    def clear_history(self):
        self.history = []
    
    def on_back(self):
        if (len(self.history) > 0):
            last_route_name = self.history.pop()
            last_route = self.get_route(last_route_name)
            self.update_current_view(last_route)

    def go_to_route(self, next_route_name, props={}):
        next_route = self.get_route(next_route_name)
        self.history.append(self.current_route['name'])
        self.update_current_view(next_route, props=props)

    def update_current_view(self, route, props={}):
        self.current_view.destroy()
        self.current_route = route
        self.update_current_component_tree(self.current_route, props)
        self.current_view.render(self.current_view.current_component_tree)

    def update_current_component_tree(self, route, props={}):
        self.current_view.update_root_options(
            route['component'], route['name'], props
        )
        self.current_view.current_component_tree = self.current_view.create_component_tree(
            route['component'], route['name'], props
        )
