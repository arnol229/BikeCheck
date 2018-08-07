import copy

class GZFrameVirtualView:
    def __init__(self, app, nav, view):
        self.app = app
        self.nav = nav
        self.view = view

    def update_view_on_state_change(self):
        pass
        # virtual_component_tree  = self.view.create_component_tree(
        #     self.view.root_options['component'], self.view.root_options['name'], self.view.root_options['props']
        # )
        # self.update_component_tree(virtual_component_tree, self.view.get_elements())

        # virtual_component_tree = None

    def update_component_tree(self, current_component, view_elements):
        matched_component = next((x for x in view_elements if x.id == current_component.id), None)
        # print('matched', matched_component)
        # print('current', current_component)
        self.update_element_props(matched_component, current_component.element_props)
        if current_component.element_type == 'component' or current_component.element_type == 'box':
            for child in current_component.children:
                self.update_component_tree(child, view_elements)

    def update_element_props(self, component, props):
        print(component.element, component.element_name)
        component.element_props = component.create_props(props)
        for k, v in props.items():
            if self.view.is_gui_instance(component.element):
                setattr(component.element, k, v)
        self.app.update()
