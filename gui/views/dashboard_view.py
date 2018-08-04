class DashboardView:
    def __init__(self, core):
        self.core = core
        self.header_text = self.core.create('text', self.core.app, text="Available Bikes", size=30, font="Times New Roman", color="lightblue", grid=[])