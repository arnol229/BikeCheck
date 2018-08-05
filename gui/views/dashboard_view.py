from framework.gzframe_view import GZFrameView

class DashboardView(GZFrameView):
    def __init__(self, gzframe):
        super().__init__(gzframe)
        self.ui.render_text(element_name='header_text', text="Available Bikes", size=30, font="Times New Roman", color="lightblue", grid=[])