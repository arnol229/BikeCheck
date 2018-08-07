from framework.gzframe_component import GZFrameComponent
from framework.gzframe_elements import GZFrameButton, GZFrameText, GZFrameContainer

class EnterPinComponent(GZFrameComponent):
    def __init__(self, element_name, state={}, props={}):
        super().__init__(element_name, state=state, props=props)

    def on_pin_entry(self, event_data):
        numeric_key_group = self.gzframe.element_by_name('numeric_key_group')
        validate_button = self.gzframe.element_by_name('validate_button')
        clear_button = self.gzframe.element_by_name('clear_button')
        pin_input = self.gzframe.element_by_name('pin_input')
        pin_error = self.gzframe.element_by_name('pin_error')
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
        pin_input = self.gzframe.element_by_name('pin_input')
        pin_error = self.gzframe.element_by_name('pin_error')
        if (pin_input.value != '1111'):
            pin_error.visible = True
            self.reset_form()
        else:
            self.state.is_authenticated = True
            self.go_to_route('dashboard')

    def update_name(self):
        self.gzframe.set_state({'name': 'Tom'})

    def clear_pin(self):
        self.reset_form()
        self.gzframe.element_by_name('pin_error').visible = False

    def reset_form(self):
        self.gzframe.element_by_name('pin_input').value = ""
        self.gzframe.element_by_name('validate_button').disable()
        self.gzframe.element_by_name('clear_button').disable()
        self.gzframe.element_by_name('numeric_key_group').enable()

    def render(self):
        welcome_message = "Welcome {name}".format(name=self.state.name)
        font = 'Times New Roman'
        numeric_keys = []
        for x in range(0,10):
            numeric_key_label = str((x+1) if x < 9 else 0)
            element_name = 'numeric_button_' + numeric_key_label
            grid = [x%3, int(x/3)] if x < 9 else [1, 3]
            numeric_keys.append(
                GZFrameButton(element_name=element_name, on_click=self.on_pin_entry, props={'text': numeric_key_label, 'grid': grid})
            )

        return [
            GZFrameButton(element_name='update_name', props={'command': self.update_name, 'text': 'Update Name'}),
            GZFrameContainer(element_name='app_controls_group', children=[
                GZFrameButton(element_name='back_button', props={'command': self.on_back, 'text': 'Back'}),
            ]),
            GZFrameText(element_name='header_text', props={'text': welcome_message, 'size': 40, 'font': font, 'color':'lightblue'}),
            GZFrameText(element_name='pin_text', props={'text': 'Enter your PIN to validate', 'size': 30, 'font': font, 'color':'lightblue'}),
            GZFrameText(element_name='pin_input', props={'text': '', 'size': 60, 'font': font, 'color':'black'}),
            GZFrameContainer(element_name='error_box', children=[
                GZFrameText(element_name='pin_error', props={'text': 'The pin is invalid', 'visible': False, 'color':'red'}),
            ]),
            GZFrameContainer(element_name='control_buttons_group', children=[
                GZFrameButton(element_name="validate_button", props={"text":"Validate", "command": self.validate_pin, 'enabled': False, 'grid': [0,0]}),
                GZFrameButton(element_name="clear_button", props={"text":"Clear", "command": self.clear_pin, 'enabled': False, 'grid': [1,0]})
            ], props={'layout': 'grid'}),
            GZFrameContainer(element_name='numeric_key_group', children=numeric_keys, props={'layout': 'grid'})
        ]