from framework.gzframe_controller import GZFrameController
from framework.gzframe_element import GZFrameButton, GZFrameText, GZFrameContainer

class DashboardCtrl(GZFrameController):
    def __init__(self, gzframe):
        super().__init__(gzframe)

        print(self.state.is_authenticated)

    def on_init(self):
        self.reset_history()

    def logout(self):
        self.state.is_authenticated = False
        self.go_to_route('welcome')

    def render(self, state):
        available_bikes = []
        for x in range(0, 5):
            element_name = "bike_item" + str(x)
            bike_text = "Bike #" + str(x + 1)
            available_bikes.append(
                GZFrameText(element_name=element_name, element_props={"text":bike_text, "size":20, "font":"Times New Roman", "color":"black"})
            )
        return [
            GZFrameButton(element_name="logout_button", element_props={"text":"Log Out", "command": self.logout}),
            GZFrameText(element_name="header_text", element_props={"text":"Available Bikes", "size":30, "font":"Times New Roman", "color":"lightblue"}),
            GZFrameContainer(element_name="bike_list_group", children=available_bikes),
            GZFrameButton(element_name="checkout_button", element_props={"text":"Check Out"})
        ]