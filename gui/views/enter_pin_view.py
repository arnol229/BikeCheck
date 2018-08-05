from framework.gzframe_view import GZFrameView

class EnterPinView(GZFrameView):
    def __init__(self, gzframe):
        super().__init__(gzframe)
        self.ui.render_text(element_name="header_text", text="Welcome PERSON", size=40, font="Times New Roman", color="lightblue", grid=[])
        self.ui.render_text(element_name="pin_text", text="Enter your PIN to validate", size=30, font="Times New Roman", color="lightblue", grid=[])
        self.ui.render_text(element_name="pin_input", text="", size=60, font="Times New Roman", color="black")

        self.ui.render_box(element_name="error_box")
        self.ui.render_text(element_name="pin_error", parent_name='error_box', text="The pin is invalid", visible=False, color="red")

        self.ui.render_box(element_name="control_buttons_box", layout="grid")
        self.ui.render_button(element_name="validate_button", parent_name="control_buttons_box", text="Validate", command=self.validate_pin, enabled=False, grid=[0,0])
        self.ui.render_button(element_name="clear_button", parent_name="control_buttons_box", text="Clear", command=self.clear_pin, enabled=False, grid=[1, 0])

        self.ui.render_box(element_name="numeric_key_box", layout="grid")

        self.ui.render_button(element_name="one_button", parent_name="numeric_key_box", on_click=self.on_pin_entry, text="1", grid=[0,0])
        self.ui.render_button(element_name="two_button", parent_name="numeric_key_box", on_click=self.on_pin_entry, text="2", grid=[1,0])
        self.ui.render_button(element_name="three_button", parent_name="numeric_key_box", on_click=self.on_pin_entry, text="3", grid=[2,0])
        self.ui.render_button(element_name="four_button", parent_name="numeric_key_box", on_click=self.on_pin_entry, text="4", grid=[0,1])
        self.ui.render_button(element_name="five_button", parent_name="numeric_key_box", on_click=self.on_pin_entry, text="5", grid=[1,1])
        self.ui.render_button(element_name="six_button", parent_name="numeric_key_box", on_click=self.on_pin_entry, text="6", grid=[2,1])
        self.ui.render_button(element_name="seven_button", parent_name="numeric_key_box", on_click=self.on_pin_entry, text="7", grid=[0,2])
        self.ui.render_button(element_name="eight_button", parent_name="numeric_key_box", on_click=self.on_pin_entry, text="8", grid=[1,2])
        self.ui.render_button(element_name="nine_button", parent_name="numeric_key_box", on_click=self.on_pin_entry, text="9", grid=[2,2])
        self.ui.render_button(element_name="zero_button", parent_name="numeric_key_box", on_click=self.on_pin_entry, text="0", grid=[1,3])

    def on_pin_entry(self, event_data):
        numeric_key_box = self.ui.element('numeric_key_box')
        validate_button = self.ui.element('validate_button')
        clear_button = self.ui.element('clear_button')
        pin_input = self.ui.element('pin_input')
        pin_error = self.ui.element('pin_error')
        if (numeric_key_box.enabled == True):
            clear_button.enable()
            pin_error.visible = False
            pin_input.value = pin_input.value + str(event_data.widget.text)

            if (len(pin_input.value) < 4):
                validate_button.disable()
            else:
                numeric_key_box.disable()
                validate_button.enable()
    
    def validate_pin(self):
        pin_input = self.ui.element('pin_input')
        pin_error = self.ui.element('pin_error')
        if (pin_input.value != '1111'):
            pin_error.visible = True
            self.reset_form()
        else:
            self.go_to_view('dashboard')

    def clear_pin(self):
        self.reset_form()
        self.ui.element('pin_error').visible = False

    def reset_form(self):
        self.ui.element('pin_input').value = ""
        self.ui.element('validate_button').disable()
        self.ui.element('clear_button').disable()
        self.ui.element('numeric_key_box').enable()