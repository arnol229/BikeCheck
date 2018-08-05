from framework.gzframe import GZFrame
from views.welcome_view import WelcomeView
from views.enter_pin_view import EnterPinView
from views.no_recognition_view import NoRecognitionView
from views.dashboard_view import DashboardView

class BikeCheckState:
    def __init__(self):
        self.is_authenticated = False
        self.auth_token = None
        self.user_id = None
        self.name = 'Christian'
        self.is_back_enabled = True

class BikeCheck:
    def __init__(self):
        self.views_config = {
            'welcome': WelcomeView,
            'enter_pin': EnterPinView,
            'no_recognition': NoRecognitionView,
            'dashboard': DashboardView
        }
        self.app_config = {
            'title': 'Bike Check',
            'width': 800,
            'height': 480
        }
        self.bikecheck = GZFrame(app_config=self.app_config, views_config=self.views_config, root_view_name='welcome', state=BikeCheckState())


app = BikeCheck()
app.bikecheck.run()

