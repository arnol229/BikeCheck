from framework.gzframe import GZFrame
from controllers.welcome_ctrl import WelcomeCtrl
from controllers.enter_pin_ctrl import EnterPinCtrl
from controllers.no_recognition_ctrl import NoRecognitionCtrl
from controllers.dashboard_ctrl import DashboardCtrl

class BikeCheckState:
    def __init__(self):
        self.is_authenticated = False
        self.auth_token = None
        self.user_id = None
        self.name = 'Christian'
        self.is_back_enabled = True

class BikeCheck:
    def __init__(self):
        self.routes = [
            {'name': 'welcome', 'controller': WelcomeCtrl, 'is_root': True},
            {'name': 'no_recognition', 'controller': NoRecognitionCtrl},
            {'name': 'enter_pin', 'controller': EnterPinCtrl},
            {'name': 'dashboard', 'controller': DashboardCtrl},
        ]
        self.app_config = {
            'title': 'Bike Check',
            'width': 800,
            'height': 480
        }
        self.bikecheck = GZFrame(app_config=self.app_config, routes=self.routes, state=BikeCheckState())


app = BikeCheck()
app.bikecheck.run()

