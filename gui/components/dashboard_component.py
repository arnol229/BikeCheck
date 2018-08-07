from framework.gzframe_component import GZFrameComponent
from framework.gzframe_elements import GZFrameButton, GZFrameText, GZFrameContainer

class DashboardComponent(GZFrameComponent):
    def __init__(self, component_name, props={}, state={}, element_props={}):
        super().__init__(component_name, props=props, state=state, element_props=element_props)

    def on_init(self):
        self.reset_history()

    def logout(self):
        self.state.is_authenticated = False
        self.go_to_route('welcome')

    def to_maintenance(self):
        self.go_to_route('maintenance')

    def render(self, props, state):
        def get_available_bikes():
            available_bikes = []
            for x in range(0, 5):
                num = str(x)
                available_bikes.append(
                    GZFrameContainer(element_name=("bike_item_group_" + num), children=[
                        GZFrameText(element_name=("bike_group_" + num), element_props={"text":("Bike #" + str(x + 1)), "size":20, "font":"Times New Roman", "color":"black", "grid": [0,0]}),
                        GZFrameText(element_name=("bike_item_status_" + num), element_props={"text":"Available", "size":20, "font":"Times New Roman", "color":"black", "grid": [1,0]})
                    ], element_props={'layout': 'grid'})
                )
            return available_bikes

        return [
            GZFrameButton(element_name="logout_button", element_props={"text":"Log Out", "command": self.logout}),
            GZFrameText(element_name="header_text", element_props={"text":"Available Bikes", "size":30, "font":"Times New Roman", "color":"lightblue"}),
            GZFrameContainer(element_name="bike_list_group", children=get_available_bikes()),
            GZFrameButton(element_name="checkout_button", element_props={"text":"Check Out"}),
            GZFrameButton(element_name="maintenance_button", element_props={"text":"Maintenance", "command": self.to_maintenance})
        ]