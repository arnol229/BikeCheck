from framework.gzframe_component import GZFrameComponent
from framework.gzframe_elements import GZFrameButton, GZFrameText, GZFrameContainer
from components.bike_list_component import BikeListComponent

class DashboardComponent(GZFrameComponent):
    def __init__(self, element_name, props={}, state={}, element_props={}):
        super().__init__(element_name, props=props, state=state, element_props=element_props)

    def on_init(self):
        self.reset_history()

    def logout(self):
        self.state.is_authenticated = False
        self.go_to_route('welcome')

    def to_maintenance(self):
        self.go_to_route('maintenance')

    def render(self, props, state):
        def get_bike_list():
            return {
                'bike_list': [{
                    'text': 'Mountain Bike',
                    'availability': 'Available'
                }]
            }

        bike_list = get_bike_list()

        return [
            GZFrameButton(element_name="logout_button", element_props={"text":"Log Out", "command": self.logout}),
            GZFrameText(element_name="header_text", element_props={"text":"Available Bikes", "size":30, "font":"Times New Roman", "color":"lightblue"}),
            BikeListComponent(element_name="bike_list", props=bike_list),
            GZFrameButton(element_name="checkout_button", element_props={"text":"Check Out"}),
            GZFrameButton(element_name="maintenance_button", element_props={"text":"Maintenance", "command": self.to_maintenance})
        ]