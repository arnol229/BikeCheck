
from guizero import Text, TextBox, PushButton, Slider, Picture, Box
from framework.gzframe_element import GZFrameElement

class GZFrameUI:
    gui_classes = [Text, TextBox, PushButton, Slider, Picture, Box]

    def __init__(self, gzframe):
        self.gzframe = gzframe
        self.elements = {'container': GZFrameElement('app', Box(self.gzframe.app), True)}

    def element(self, name):
        return getattr(self.elements[name], 'element')

    def set_element(self, element_name, parent_name, element, is_box = False):
        self.elements[element_name] = GZFrameElement(parent_name, element, is_box)

    def get_box(self, box_name = None):
        return (self.element('container') if box_name is None else self.element(box_name))

    def render_box(self, element_name, parent_name = None, *args, **kwargs):
        element = Box(self.get_box(parent_name), *args, **kwargs)
        self.set_element(element_name, parent_name, element, True)

    def render_text(self, element_name, parent_name = None, *args, **kwargs):
        element = Text(self.get_box(parent_name), *args, **kwargs)
        self.set_element(element_name, parent_name, element)

    def render_button(self, element_name, parent_name = None, on_click = None, *args, **kwargs):
        element = PushButton(self.get_box(parent_name), *args, **kwargs)
        if not (on_click is None):
            element.when_clicked = on_click
        self.set_element(element_name, parent_name, element)

    def render_input(self, element_name, parent_name = None, *args, **kwargs):
        element = TextBox(self.get_box(parent_name), *args, **kwargs)
        self.set_element(element_name, parent_name, element)

    def start_loop(self, interval, func, element_name = None):
        box = self.get_box(element_name)
        box.repeat(interval, func)

    def cancel_loop(self, func, element_name = None):
        box = self.get_box(element_name)
        box.cancel(func)