class EnterPinView:
    def __init__(self, core):
        self.core = core
        self.header_text = self.core.create('text', self.core.app, text="Welcome PERSON", size=40, font="Times New Roman", color="lightblue", grid=[])
        self.pin_text = self.core.create('text', self.core.app, text="Enter your PIN to validate", size=30, font="Times New Roman", color="lightblue", grid=[])
        self.pin_input = self.core.create('text', self.core.app, text="", size=60, font="Times New Roman", color="black")

        self.error_box = self.core.create('box', self.core.app)
        self.pin_error = self.core.create('text', self.error_box, text="The pin is invalid", visible=False, color="red")

        self.control_buttons_box = self.core.create('box', self.core.app, layout="grid")
        self.validate_button = self.core.create('push_button', self.control_buttons_box, text="Validate", command=self.validate_pin, enabled=False, grid=[0,0])
        self.clear_button = self.core.create('push_button', self.control_buttons_box, text="Clear", command=self.clear_pin, enabled=False, grid=[1, 0])

        self.numeric_key_box = self.core.create('box', self.core.app, layout="grid")

        self.one_button = self.core.create('push_button', self.numeric_key_box, text="1", grid=[0,0])
        self.two_button = self.core.create('push_button', self.numeric_key_box, text="2", grid=[1,0])
        self.three_button = self.core.create('push_button', self.numeric_key_box, text="3", grid=[2,0])
        self.four_button = self.core.create('push_button', self.numeric_key_box, text="4", grid=[0,1])
        self.five_button = self.core.create('push_button', self.numeric_key_box, text="5", grid=[1,1])
        self.six_button = self.core.create('push_button', self.numeric_key_box, text="6", grid=[2,1])
        self.seven_button = self.core.create('push_button', self.numeric_key_box, text="7", grid=[0,2])
        self.eight_button = self.core.create('push_button', self.numeric_key_box, text="8", grid=[1,2])
        self.nine_button = self.core.create('push_button', self.numeric_key_box, text="9", grid=[2,2])
        self.zero_button = self.core.create('push_button', self.numeric_key_box, text="0", grid=[1,3])

        self.one_button.when_clicked = self.on_pin_entry
        self.two_button.when_clicked = self.on_pin_entry
        self.three_button.when_clicked = self.on_pin_entry
        self.four_button.when_clicked = self.on_pin_entry
        self.five_button.when_clicked = self.on_pin_entry
        self.six_button.when_clicked = self.on_pin_entry
        self.seven_button.when_clicked = self.on_pin_entry
        self.eight_button.when_clicked = self.on_pin_entry
        self.nine_button.when_clicked = self.on_pin_entry
        self.zero_button.when_clicked = self.on_pin_entry

    def on_pin_entry(self, event_data):
        if (self.numeric_key_box.enabled == True):
            self.clear_button.enable()
            self.pin_error.visible = False
            self.pin_input.value = self.pin_input.value + str(event_data.widget.text)

            if (len(self.pin_input.value) < 4):
                self.validate_button.disable()
            else:
                self.numeric_key_box.disable()
                self.validate_button.enable()
    
    def validate_pin(self):
        if (self.pin_input.value != '1212'):
            self.pin_error.visible = True
            self.reset_form()
        else:
            self.core.nav.go_to_view('dashboard', True)

    def clear_pin(self):
        self.reset_form()
        self.pin_error.visible = False

    def reset_form(self):
        self.pin_input.value = ""
        self.validate_button.disable()
        self.clear_button.disable()
        self.numeric_key_box.enable()