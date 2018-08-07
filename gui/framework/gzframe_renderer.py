
from guizero import Text, PushButton, Box

class GZFrameRenderer:
    gui_classes = [Text, PushButton, Box]

    def __init__(self, gzframe):
        self.gzframe = gzframe
        self.elements = {}

    def render(self, current_element, parent, index = 0):
        current_element.index = index
        if current_element.element_type == 'component':
            current_element.element = Box(parent, **current_element.element_props)
            current_element.gzframe = self.gzframe
            current_element.on_init()
            for child_index, child in enumerate(current_element.children):
                self.render(child, current_element.element, child_index)
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

    def destroy(self):
        for element_name in self.elements:
            for g_class in self.gui_classes:
                element_class = self.elements[element_name]
                element = getattr(element_class, 'element')
                if isinstance(element, g_class):
                    element.destroy()
                element = None
            self.elements[element_name] = None
        self.elements = {}

    def element(self, name):
        return getattr(self.elements[name], 'element')