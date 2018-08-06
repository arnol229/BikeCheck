class GZFrameCore:

    def __init__(self, gzframe, routes):
        self.gzframe = gzframe
        self.history = []
        self.routes = routes
        self.root_route = self.get_root(routes)
        self.current_route = None
        self.current_view = None

    def initialize(self):
        self.current_route = self.root_route
        self.current_view = self.current_route['controller'](self.gzframe)

    def get_root(self, routes):
        root_controller = None
        for route in routes:
            if 'is_root' in route:
                if route['is_root'] is True:
                    root_controller = route

        if not (root_controller is None):
            return routes[0]
        else:
            return root_controller
    
    def get_route(self, route_name):
        return next(
            (ctrl for ctrl in self.routes if ctrl['name'] == route_name), self.root_route
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

    def go_to_route(self, next_route_name):
        next_route = self.get_route(next_route_name)
        self.history.append(self.current_route['name'])
        self.update_current_view(next_route)

    def update_current_view(self, route):
        self.destroy_current_view()
        self.current_route = route
        self.current_view = self.current_route['controller'](self.gzframe)

    def destroy_current_view(self):
        for element_name in self.current_view.view.elements:
            for g_class in self.current_view.view.gui_classes:
                element_class = self.current_view.view.elements[element_name]
                element = getattr(element_class, 'element')
                if isinstance(element, g_class):
                    element.destroy()
                element = None
            self.current_view.view.elements[element_name] = None

    def without_keys(self, d, keys):
        return {x: d[x] for x in d if x not in keys}
