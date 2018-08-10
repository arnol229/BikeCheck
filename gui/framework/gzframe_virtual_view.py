import copy

class GZFrameVirtualView:
    def __init__(self, app, nav, view):
        self.app = app
        self.nav = nav
        self.view = view
        self.update_mapping = {
            'text': {'text': 'value', 'enabled': 'enabled', 'size': 'text_size', 'color': 'text_color'},
            'button': {'text': 'text', 'enabled': 'enabled', 'size': 'text_size', 'color': 'text_color'}
        }

    def update_view_on_state_change(self):
        virtual_component_tree  = self.view.create_component_tree(
            self.view.root_options['component'], self.view.root_options['name'], self.view.root_options['props']
        )
        self.update_component_tree(virtual_component_tree, self.view.get_elements())
        self.app.update()

    def update_component_tree(self, current_component, view_elements):
        matched_component = next((x for x in view_elements if x.id == current_component.id), None)
        self.update_props(matched_component, current_component.props)
        if current_component.element_type == 'component' or current_component.element_type == 'box':
            for child in current_component.children:
                self.update_component_tree(child, view_elements)

    def update_props(self, component, props):
        component.props = component.merge_two_dicts(component.with_callable(component.props), component.without_callable(props))
        for k, v in props.items():
            if self.view.is_gui_instance(component.element):
                if component.element_type in self.update_mapping:
                    element_type = self.update_mapping[component.element_type]
                    if k in element_type:
                        setattr(component.element, element_type[k], v)

        if component.element_type == 'component':
            component.gz_on_change()

