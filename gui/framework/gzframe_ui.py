
from guizero import Text, TextBox, PushButton, Slider, Picture, Box
from framework.gzframe_element import GZFrameElement

class GZFrameUI:
    def __init__(self, gzframe):
        self.gzframe = gzframe
        self.elements = {'root': GZFrameElement('app', Box(self.gzframe.app), True)}

    def element(self, name):
        return getattr(self.elements[name], 'element')

    def set_element(self, element_name, parent_name, element, is_box = False):
        self.elements[element_name] = GZFrameElement(parent_name, element, is_box)

    def get_box(self, box_name = None):
        return (self.element('root') if box_name is None else self.element(box_name))

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

    def render_element_group(self, group_name, parent_name = None, elements = [], renderer = None, *args, **kwargs):
        self.render_box(group_name, parent_name, *args, **kwargs)
        for index in range(0, len(elements)):
            name_key = 'element_name'
            renderer_key = 'renderer'
            element = elements[index]
            element[name_key] = (element[name_key] if name_key in element else group_name + str(index))
            render = (element[renderer_key] if renderer_key in element else renderer)
            render(parent_name=group_name, **self.gzframe.core.without_keys(element, {'renderer'}))