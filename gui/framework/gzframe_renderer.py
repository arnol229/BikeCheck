
from guizero import Text, PushButton, Box
from framework.gzframe_elements import GZFrameElement

class GZFrameRenderer:
    gui_classes = [Text, PushButton, Box]

    def __init__(self, gzframe, state):
        self.gzframe = gzframe
        self.state = state
        self.root_options = {'name': 'root', 'component': None, 'props': {}}
        self.current_component_tree = None
        self.__elements = []

    def get_elements(self):
        return self.__elements

    def create_component_tree(self, component, name, props={}):
        GZFrameElement.reset_count()
        return component(name, props=props, state=self.state)

    def update_root_options(self, component, name='root', props={}):
        self.root_options['component'] = component
        self.root_options['name'] = name
        self.root_options['props'] = props

    def render(self, current_element, parent, index = 0):
        current_element.index = index
        if current_element.element_type == 'component':
            current_element.element = Box(parent)
            current_element.gzframe = self.gzframe
            current_element.gz_on_init()
            for child_index, child in enumerate(current_element.children):
                self.render(child, current_element.element, child_index)
        if current_element.element_type == 'box':
            current_element.element = Box(parent, **current_element.props)
            for child_index, child in enumerate(current_element.children):
                self.render(child, current_element.element, child_index)
        elif current_element.element_type == 'text':
            current_element.element = Text(parent, **current_element.props)
        elif current_element.element_type == 'button':
            current_element.element = PushButton(parent, **current_element.props)
            if not (current_element.on_click is None):
                current_element.element.when_clicked = current_element.on_click
        
        self.__elements.append(current_element)

    def destroy(self):
        for index, gz_element in enumerate(self.__elements):
            element = getattr(gz_element, 'element')
            if self.is_gui_instance(element):
                if gz_element.element_type == 'component':
                    gz_element.gz_on_destroy()
                element.destroy()
            element = None
            self.__elements[index] = None
        self.__elements = []
        self.current_component_tree = None

    def element_by_name(self, name):
        return getattr(self.component(name), 'element')

    def is_gui_instance(self, element):
        return next((True for g_class in self.gui_classes if isinstance(element, g_class)), False)

    def component(self, name):
        return next((component for component in self.__elements if component.element_name == name), None)