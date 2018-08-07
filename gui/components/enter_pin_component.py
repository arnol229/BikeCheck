from framework.gzframe_component import GZFrameComponent
from framework.gzframe_elements import GZFrameButton, GZFrameText, GZFrameContainer

class EnterPinComponent(GZFrameComponent):
    def __init__(self, element_name, props={}, state={}, element_props={}):
        super().__init__(element_name, props=props, state=state, element_props=element_props)

    def on_pin_entry(self, event_data):
        numeric_key_group = self.gzframe.element('numeric_key_group')
        validate_button = self.gzframe.element('validate_button')
        clear_button = self.gzframe.element('clear_button')
        pin_input = self.gzframe.element('pin_input')
        pin_error = self.gzframe.element('pin_error')
        if (numeric_key_group.enabled == True):
            clear_button.enable()
            pin_error.visible = False
            pin_input.value = pin_input.value + str(event_data.widget.text)

            if (len(pin_input.value) < 4):
                validate_button.disable()
            else:
                numeric_key_group.disable()
                validate_button.enable()
    
    def validate_pin(self):
        pin_input = self.gzframe.element('pin_input')
        pin_error = self.gzframe.element('pin_error')
        if (pin_input.value != '1111'):
            pin_error.visible = True
            self.reset_form()
        else:
            self.state.is_authenticated = True
            self.go_to_route('dashboard')

    def clear_pin(self):
        self.reset_form()
        self.gzframe.element('pin_error').visible = False

    def reset_form(self):
        self.gzframe.element('pin_input').value = ""
        self.gzframe.element('validate_button').disable()
        self.gzframe.element('clear_button').disable()
        self.gzframe.element('numeric_key_group').enable()

    def render(self, props, state):
        welcome_message = "Welcome {name}".format(name=state.name)
        font = 'Times New Roman'
        numeric_keys = []
        for x in range(0,10):
            numeric_key_label = str((x+1) if x < 9 else 0)
            element_name = 'numeric_button_' + numeric_key_label
            grid = [x%3, int(x/3)] if x < 9 else [1, 3]
            numeric_keys.append(
                GZFrameButton(element_name=element_name, on_click=self.on_pin_entry, element_props={'text': numeric_key_label, 'grid': grid})
            )

        return [
            GZFrameContainer(element_name='app_controls_group', children=[
                GZFrameButton(element_name='back_button', element_props={'command': self.on_back, 'text': 'Back'}),
            ]),
            GZFrameText(element_name='header_text', element_props={'text': welcome_message, 'size': 40, 'font': font, 'color':'lightblue'}),
            GZFrameText(element_name='pin_text', element_props={'text': 'Enter your PIN to validate', 'size': 30, 'font': font, 'color':'lightblue'}),
            GZFrameText(element_name='pin_input', element_props={'text': '', 'size': 60, 'font': font, 'color':'black'}),
            GZFrameContainer(element_name='error_box', children=[
                GZFrameText(element_name='pin_error', element_props={'text': 'The pin is invalid', 'visible': False, 'color':'red'}),
            ]),
            GZFrameContainer(element_name='control_buttons_group', children=[
                GZFrameButton(element_name="validate_button", element_props={"text":"Validate", "command": self.validate_pin, 'enabled': False, 'grid': [0,0]}),
                GZFrameButton(element_name="clear_button", element_props={"text":"Clear", "command": self.clear_pin, 'enabled': False, 'grid': [1,0]})
            ], element_props={'layout': 'grid'}),
            GZFrameContainer(element_name='numeric_key_group', children=numeric_keys, element_props={'layout': 'grid'})
        ]