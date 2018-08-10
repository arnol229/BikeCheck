from framework.gzframe import GZFrame
from components.welcome_component import WelcomeComponent
from components.no_recognition_component import NoRecognitionComponent
from components.dashboard_component import DashboardComponent
from components.maintenance_component import MaintenanceComponent
from components.verify_component import VerifyComponent

class BikeCheck:
    def __init__(self):
        self.routes = [
            {'name': 'welcome', 'component': WelcomeComponent, 'is_root': True},
            {'name': 'verify', 'component':VerifyComponent},
            {'name': 'dashboard', 'component': DashboardComponent},
            {'name': 'maintenance', 'component': MaintenanceComponent},
        ]
        self.app_config = {
            'title': 'Bike Check',
            'width': 800,
            'height': 480
        }
        self.state = {'auth':{}, 'is_authenticated': False, 'auth_token': None, 'user_id': None, 'name': 'Christian'}
        self.bikecheck = GZFrame(app_config=self.app_config, routes=self.routes, state=self.state)


app = BikeCheck()
app.bikecheck.run()

