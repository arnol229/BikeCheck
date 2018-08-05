
from guizero import Text, TextBox, PushButton, Slider, Picture, Box

class GZFrameUI:
    def __init__(self, gzframe):
        self.gzframe = gzframe
        self.container = Box(self.gzframe.app)

    def render_box(self, container = None, *args, **kwargs):
        if container is None:
            return Box(self.container, *args, **kwargs)
        else:
            return Box(container, *args, **kwargs)

    def render_text(self, container = None, *args, **kwargs):
        if container is None:
            return Text(self.container, *args, **kwargs)
        else:
            return Text(container, *args, **kwargs)

    def render_button(self, container = None, *args, **kwargs):
        if container is None:
            return PushButton(self.container, *args, **kwargs)
        else:
            return PushButton(container, *args, **kwargs)

    def render_input(self, container = None, *args, **kwargs):
        if container is None:
            return TextBox(self.container, *args, **kwargs)
        else:
            return TextBox(container, *args, **kwargs)

    def start_loop(self, interval, func, container = None):
        if container is None:
            self.container.repeat(interval, func)
        else:
            container.repeat(interval, func)

    def cancel_loop(self, func, container = None):
        if container is None:
            self.container.cancel(func)
        else:
            container.cancel(func)