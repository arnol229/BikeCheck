class EnterPinView:
    def __init__(self, core):
        self.core = core
        self.header_text = self.core.create('text', text="Welcome PERSON", size=40, font="Times New Roman", color="lightblue", grid=[])
        self.pin_text = self.core.create('text', text="Enter your PIN to validate", size=30, font="Times New Roman", color="lightblue", grid=[])
        self.pin_input = self.core.create('text_box', command=self.check_pin)
        self.pin_error = self.core.create('text', text="", visible=False, color="red")
        self.validate_button = self.core.create('push_button', text="Validate")
    
    def check_pin(self, enteredKey):
        currentPinEntry = self.pin_input.value + enteredKey

        if (len(currentPinEntry) < 4):
            self.pin_error.text = "The pin is invalid"
            self.pin_error.visible = True
        else:
            self.pin_error.text = ""
            self.pin_error.visible = False