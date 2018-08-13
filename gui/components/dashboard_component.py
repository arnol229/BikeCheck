from framework.gzframe_component import GZFrameComponent
from framework.gzframe_elements import GZFrameButton, GZFrameText, GZFrameContainer
from components.bike_list_component import BikeListComponent

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

class DashboardComponent(GZFrameComponent):
    def __init__(self, element_name, state={}, props={}):
        super().__init__(element_name, state=state, props=props)
        self.pin_state = 0

    def gz_on_init(self):
        self.reset_history()

    def logout(self):
        self.state.is_authenticated = False
        self.go_to_route('welcome')

    def to_maintenance(self):
        self.go_to_route('maintenance')

    def checkout_bike(self):
        if self.pin_state:
            GPIO.output(4,0)
            self.element.cancel(self.checkout_bike)
            self.pin_state = 0
        else:
            self.pin_state = 1
            GPIO.output(4,1)
            self.element.repeat(5000, self.checkout_bike)

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
            GZFrameButton(element_name="checkout_button", props={"text":"Check Out", "command":self.checkout_bike}),
            GZFrameButton(element_name="maintenance_button", props={"text":"Maintenance", "command": self.to_maintenance})
        ]