from guizero import App
from main.bike_check_core import BikeCheckCore
from views.welcome_view import WelcomeView
from views.enter_pin_view import EnterPinView
from views.no_recognition_view import NoRecognitionView
from views.dashboard_view import DashboardView

class BikeCheckApp:
    def __init__(self, app, views_config, root_view_name):
        self.core = BikeCheckCore(app=app(title="BikeCheck"), views_config=views_config, root_view_name=root_view_name)

    def run(self):
        self.core.app.display()

views_config = {
    'welcome': WelcomeView,
    'enter_pin': EnterPinView,
    'no_recognition': NoRecognitionView,
    'dashboard': DashboardView
}
app = BikeCheckApp(App, views_config, 'welcome')
app.run()

