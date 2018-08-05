from framework.gzframe_view import GZFrameView

class NoRecognitionView(GZFrameView):
    def __init__(self, gzframe):
        super().__init__(gzframe)
        self.ui.render_text(element_name='header_text', text="Can't Recognize You!", size=40, font="Times New Roman", color="lightblue", grid=[])