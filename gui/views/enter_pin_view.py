from framework.gzframe_view import GZFrameView

class EnterPinView(GZFrameView):
    def __init__(self, gzframe):
        super().__init__(gzframe)
        self.ui.render_box(element_name="app_controls_group")
        self.ui.render_button('back_button', parent_name="app_controls_group", command=self.on_back, text="Back")
        self.ui.element('app_controls_group').bg = 'red'

        welcome_message = "Welcome {name}".format(name=self.state.name)
        self.ui.render_text(element_name="header_text", text=welcome_message, size=40, font="Times New Roman", color="lightblue", grid=[])
        self.ui.render_text(element_name="pin_text", text="Enter your PIN to validate", size=30, font="Times New Roman", color="lightblue", grid=[])
        self.ui.render_text(element_name="pin_input", text="", size=60, font="Times New Roman", color="black")

        self.ui.render_box(element_name="error_box")
        self.ui.render_text(element_name="pin_error", parent_name='error_box', text="The pin is invalid", visible=False, color="red")

        control_buttons = [
            {'command': self.validate_pin, 'element_name': "validate_button", "text": "Validate", "enabled": False, 'grid': [0,0]},
            {'command': self.clear_pin, 'element_name': "clear_button", "text": "Clear", "enabled": False, 'grid': [1,0]},
        ]

        self.ui.render_element_group(renderer=self.ui.render_button, group_name="control_buttons_group", elements=control_buttons, layout="grid")

        numeric_buttons = [
            {'on_click': self.on_pin_entry, 'text': '1', 'grid': [0,0]},
            {'on_click': self.on_pin_entry, 'text': '2', 'grid': [1,0]},
            {'on_click': self.on_pin_entry, 'text': '3', 'grid': [2,0]},
            {'on_click': self.on_pin_entry, 'text': '4', 'grid': [0,1]},
            {'on_click': self.on_pin_entry, 'text': '5', 'grid': [1,1]},
            {'on_click': self.on_pin_entry, 'text': '6', 'grid': [2,1]},
            {'on_click': self.on_pin_entry, 'text': '7', 'grid': [0,2]},
            {'on_click': self.on_pin_entry, 'text': '8', 'grid': [1,2]},
            {'on_click': self.on_pin_entry, 'text': '9', 'grid': [2,2]},
            {'on_click': self.on_pin_entry, 'text': '0', 'grid': [1,3]},
        ]

        self.ui.render_element_group(renderer=self.ui.render_button, group_name="numeric_key_group", elements=numeric_buttons, layout="grid")

    def on_pin_entry(self, event_data):
        numeric_key_group = self.ui.element('numeric_key_group')
        validate_button = self.ui.element('validate_button')
        clear_button = self.ui.element('clear_button')
        pin_input = self.ui.element('pin_input')
        pin_error = self.ui.element('pin_error')
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
        pin_input = self.ui.element('pin_input')
        pin_error = self.ui.element('pin_error')
        if (pin_input.value != '1111'):
            pin_error.visible = True
            self.reset_form()
        else:
            self.state.is_authenticated = True
            self.go_to_view('dashboard')

    def clear_pin(self):
        self.reset_form()
        self.ui.element('pin_error').visible = False

    def reset_form(self):
        self.ui.element('pin_input').value = ""
        self.ui.element('validate_button').disable()
        self.ui.element('clear_button').disable()
        self.ui.element('numeric_key_group').enable()