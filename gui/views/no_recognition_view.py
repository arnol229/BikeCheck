from framework.gzframe_view import GZFrameView

class NoRecognitionView(GZFrameView):
    def __init__(self, gzframe):
        super().__init__(gzframe)
        self.ui.render_box(element_name="app_controls_group")
        self.ui.render_button('back_button', parent_name="app_controls_group", command=self.on_back, text="Back")
        self.ui.element('app_controls_group').bg = 'red'

        self.ui.render_text(element_name='header_text', text="Can't Recognize You!", size=40, font="Times New Roman", color="lightblue", grid=[])