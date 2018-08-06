
from guizero import Text, PushButton, Box
from framework.gzframe_element import GZFrameContainer

class GZFrameView:
    gui_classes = [Text, PushButton, Box]

    def __init__(self, gzframe, template):
        self.gzframe = gzframe
        self.elements = {}
        self.template = GZFrameContainer(element_name='root', children=template)
        self.render(self.template, parent=self.gzframe.app)

    def render(self, current_element, parent, index = 0):
        current_element.index = index
        if current_element.element_type == 'box':
            current_element.element = Box(parent, **current_element.element_props)
            for child_index, child in enumerate(current_element.children):
                self.render(child, current_element.element, child_index)
        elif current_element.element_type == 'text':
            current_element.element = Text(parent, **current_element.element_props)
        elif current_element.element_type == 'button':
            current_element.element = PushButton(parent, **current_element.element_props)
            if not (current_element.on_click is None):
                current_element.element.when_clicked = current_element.on_click
        
        self.elements[current_element.element_name] = current_element

    def element(self, name):
        return getattr(self.elements[name], 'element')