from framework.gzframe_component import GZFrameComponent
from framework.gzframe_elements import GZFrameButton, GZFrameText, GZFrameContainer
from components.bike_list_component import BikeListComponent

class DashboardComponent(GZFrameComponent):
    def __init__(self, element_name, state={}, props={}):
        super().__init__(element_name, state=state, props=props)

    def gz_on_init(self):
        self.reset_history()

    def logout(self):
        self.state.is_authenticated = False
        self.go_to_route('welcome')

    def to_maintenance(self):
        self.go_to_route('maintenance')

    def render(self, state):
        def get_bike_list():
            return {
                'bike_list': [{
                    'text': 'Mountain Bike',
                    'availability': 'Available'
                }]
            }

        bike_list = get_bike_list()

        return [
            GZFrameButton(element_name="logout_button", props={"text":"Log Out", "command": self.logout}),
            GZFrameText(element_name="header_text", props={"text":"Available Bikes", "size":30, "font":"Times New Roman", "color":"lightblue"}),
            BikeListComponent(element_name="bike_list", props=bike_list, state=state),
            GZFrameButton(element_name="checkout_button", props={"text":"Check Out"}),
            GZFrameButton(element_name="maintenance_button", props={"text":"Maintenance", "command": self.to_maintenance})
        ]