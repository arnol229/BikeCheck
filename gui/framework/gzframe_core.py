from framework.gzframe_renderer import GZFrameRenderer

class GZFrameCore:

    def __init__(self, gzframe, routes):
        self.gzframe = gzframe
        self.history = []
        self.routes = routes
        self.root_route = self.get_root_route(routes)
        self.root_component = None
        self.current_route = None
        self.current_view = GZFrameRenderer(self.gzframe)

    def get_root_route(self, routes):
        root_route = None
        for route in routes:
            if 'is_root' in route:
                if route['is_root'] is True:
                    root_route = route

        if not (root_route is None):
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
            self.current_view.destroy()
            self.update_current_view(last_route)

    def go_to_route(self, next_route_name, props={}):
        next_route = self.get_route(next_route_name)
        self.history.append(self.current_route['name'])
        self.current_view.destroy()
        self.update_current_view(next_route, props)

    def update_current_view(self, route, props={}):
        self.current_route = route
        self.root_component = self.current_route['component'](self.current_route['name'], props, state=self.gzframe.state)
        self.current_view.render(self.root_component, self.gzframe.app)

    def without_keys(self, d, keys):
        return {x: d[x] for x in d if x not in keys}
