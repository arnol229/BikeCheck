from guizero import App, Text, PushButton, Box, Picture
from framework.gzframe_elements import GZFrameElement
from framework.gzframe_utils import includes, find

class GZFrameRenderer:
    gui_classes = [Text, PushButton, Box, Picture]

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

    def render(self, current_component, parent_component=None):
        self.render_node(current_component, parent_component)

    def render_node(self, current_component, parent_component=None, parent_chain='app', index = 0):
        if self.name_exists(current_component.element_name):
            raise ValueError('An element with the name "' + current_component.element_name + '" already exists!')
        parent = self.gzframe.app if parent_component is None else parent_component.element

        current_component.parent = self.gzframe.app if parent_component is None else parent_component.element
        current_component.parent_name = 'app' if parent_component is None else parent_component.element_name
        current_component.parent_chain =  parent_chain
        current_component.index = index

        if current_component.element_type == 'component':
            current_component.element = Box(parent)
            current_component.gzframe = self.gzframe
            current_component.gz_on_init()
            for child_index, child in enumerate(current_component.children):
                self.render_node(child, current_component, parent_chain=(parent_chain + '>' + current_component.element_name), index=child_index)
        if current_component.element_type == 'box':
            current_component.element = Box(parent, **current_component.props)
            for child_index, child in enumerate(current_component.children):
                self.render_node(child, current_component, parent_chain=(current_component.parent_chain + '>' + current_component.element_name), index=child_index)
        elif current_component.element_type == 'text':
            current_component.element = Text(parent, **current_component.props)
        elif current_component.element_type == 'button':
            current_component.element = PushButton(parent, **current_component.props)
            if not (current_component.on_click is None):
                current_component.element.when_clicked = current_component.on_click
        elif current_component.element_type == 'picture':
            current_component.element = Picture(parent, **current_component.props)
        
        self.__elements.append(current_component)

    def destroy(self, element_name=None):
        elements_to_destroy = list(self.__elements) if element_name is None else self.find_elements_by_parent_chain(element_name)
        component = self.gzframe.app if element_name is None else self.component(element_name)

        if component is not None:
            for gz_element in elements_to_destroy:
                element = getattr(gz_element, 'element')
                if self.is_gui_instance(element):
                    if gz_element.element_type == 'component':
                        gz_element.gz_on_destroy()
                    element.destroy()
                self.__elements.remove(gz_element)
            
            if isinstance(component, App):
                self.current_component_tree = None
            else:
                if component.element_type == 'component':
                    component.gz_on_destroy()
                component.element.destroy()
                self.__elements.remove(component)
                parent_component = self.component(component.parent_name)
                parent_component.children.remove(component)
                
    def find_elements_by_parent_chain(self, element_name):
        sub_elements = []

        for gz_element in self.__elements:
            if element_name in gz_element.parent_chain.split('>'):
                sub_elements.append(gz_element)

        return sub_elements

    def name_exists(self, name):
        def find_by_name(name, component):
            return name == component.element_name
        return includes(self.__elements, name, find_by_name)

    def element_by_name(self, name):
        return getattr(self.component(name), 'element')

    def is_gui_instance(self, element):
        return includes(self.gui_classes, element, isinstance)

    def component(self, name):
        def find_by_name(name, component):
            return name == component.element_name
        return find(self.__elements, name, find_by_name)