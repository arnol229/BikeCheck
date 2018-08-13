from framework.gzframe_component import GZFrameComponent
from framework.gzframe_elements import GZFrameButton, GZFrameText, GZFrameContainer, GZFramePicture
import requests
import asyncio
import datetime

from interfaces import RFID

AUTH_URL = 'https://test-crud.azurewebsites.net/login'

class VerifyComponent(GZFrameComponent):
    def __init__(self, element_name, state={}, props={}):
        self.counter = 0
        super().__init__(element_name, state=state, props=props, width=800)

    def auth_submit(self):
        print('auth submit: ', self.state.auth)
        if len(self.state.auth.keys()) < 2:
            print("not enough auth gathered: ", self.state.auth)
            return
        self.state.auth.get('faceId')
        resp = requests.post(AUTH_URL, data={}, params={})#, data=self.state.auth['face'], params=self.state.auth['pin'])
        print("----AUTH RESP----")
        print(resp.text)
        print(resp.status_code)
        print("-----------------")
        return resp.status_code == 200

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
    
    def listen_for_rfid(self):
        print("searching for rfid")
        user_rfid = RFID.scan()
        if user_rfid:
            self.state.auth['rfid'] = user_rfid
            self.element.cancel(self.listen_for_rfid)
            self.auth_submit()

    def validate_pin(self):
        pin_input = self.gzframe.element_by_name('pin_input')
        pin_error = self.gzframe.element_by_name('pin_error')
        self.state.auth['pin'] = pin_input
        if len(self.state.auth) > 1:
            if self.auth_submit():
                self.go_to_route('dashboard')
            else:
                pin_error.value = "Not authenticated. Try again!"
                pin_error.visible = True
                self.gzframe.element_by_name('pin_input').value = ""

    def update_name(self):
        self.gzframe.set_state({'name': 'Tom'})

    def clear_pin(self):
        print(dir(self.listen_for_rfid))
        print('counter: ', self.counter)
        if 'pin' in self.state.auth:
            del self.state.auth['pin']
        self.reset_form()

    def reset_form(self):
        self.gzframe.element_by_name('pin_input').value = ""
        self.gzframe.element_by_name('validate_button').disable()
        self.gzframe.element_by_name('clear_button').disable()
        self.gzframe.element_by_name('numeric_key_group').enable()

    def render(self, state):
        welcome_message = "Welcome {name}".format(name=state.name)
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
            GZFrameContainer(element_name='layout_group', children=[
                GZFrameContainer(element_name='header_group', children=[
                    GZFrameContainer(element_name='app_controls_group', children=[
                        GZFrameButton(element_name='back_button', props={'command': self.on_back, 'text': 'Back'}),
                    ], props={'grid': [0, 0, 1, 1], 'align': 'left'}),
                    GZFrameText(element_name='header_text', props={'text': welcome_message, 'size': 40, 'font': font, 'color':'lightblue', 'grid': [1, 0]}),
                ], props={'grid': [0,0, 4, 1], 'layout': 'grid'}, width=800),

                GZFrameContainer(element_name='pin_dialog', children=[
                    GZFrameText(element_name='pin_input', props={'text': '', 'size': 40, 'font': font, 'color':'black'}),
                    GZFrameText(element_name='pin_text', props={'text': 'Enter your PIN to validate', 'size': 15, 'font': font, 'color':'lightblue'}),
                    GZFrameContainer(element_name='error_box', children=[
                        GZFrameText(element_name='pin_error', props={'text': 'The pin is invalid', 'visible': False, 'color':'red'}),
                    ]),
                    GZFrameContainer(element_name='control_buttons_group', children=[
                        GZFrameButton(element_name="validate_button", props={"text":"Validate", "command": self.validate_pin, 'enabled': False, 'grid': [0,0]}),
                        GZFrameButton(element_name="clear_button", props={"text":"Clear", "command": self.clear_pin, 'enabled': False, 'grid': [1,0]})
                    ], props={'layout': 'grid'}),
                ], props={'grid': [0,1, 4, 1]}, width=800),

                GZFrameContainer(element_name='picture_group', children=[
                    GZFramePicture(element_name="user_picture", props={'image': self.state.auth['face']}, height=200, width=200),
                ], props={'grid': [0, 2, 1, 1], 'align': 'left'}, bg='blue', width=400),

                GZFrameContainer(element_name='numeric_key_group', children=numeric_keys, props={'layout': 'grid', 'align': 'right', 'grid': [1, 2, 1, 1]}, bg='green', width=400),

                # GZFrameContainer(element_name='rfid_dialog', children=[
                #     GZFrameText(element_name='rfid_text', props={'text': 'scan your bike chip', 'size': 30, 'font': font, 'color':'lightblue'}),
                # ], props={'layout': 'auto', 'grid': [0, 2]}),
            ], props={'layout': 'grid'}, width=800)
        ]