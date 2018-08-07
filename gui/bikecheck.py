from framework.gzframe import GZFrame
from components.welcome_component import WelcomeComponent
from components.enter_pin_component import EnterPinComponent
from components.no_recognition_component import NoRecognitionComponent
from components.dashboard_component import DashboardComponent
from components.maintenance_component import MaintenanceComponent

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
            {'name': 'welcome', 'component': WelcomeComponent, 'is_root': True},
            {'name': 'no_recognition', 'component': NoRecognitionComponent},
            {'name': 'enter_pin', 'component': EnterPinComponent},
            {'name': 'dashboard', 'component': DashboardComponent},
            {'name': 'maintenance', 'component': MaintenanceComponent},
        ]
        self.app_config = {
            'title': 'Bike Check',
            'width': 800,
            'height': 480
        }
        self.bikecheck = GZFrame(app_config=self.app_config, routes=self.routes, state=BikeCheckState())


app = BikeCheck()
app.bikecheck.run()

