from guizero import Text

class NoRecognitionView:
    def __init__(self, core):
        self.core = core
        self.header_text = Text(self.core.app, text="Can't Recognize You!", size=40, font="Times New Roman", color="lightblue", grid=[])