from framework.gzframe_view import GZFrameView

class DashboardView(GZFrameView):
    def __init__(self, gzframe):
        super().__init__(gzframe)
        self.reset_history()
        self.ui.render_button(element_name="logout_button", text="Log Out", command=self.logout)
        self.ui.render_text(element_name='header_text', text="Available Bikes", size=30, font="Times New Roman", color="lightblue", grid=[])

        bike_list = [
            {'text': 'Bike #1'},
            {'text': 'Bike #2'},
            {'text': 'Bike #3'},
            {'text': 'Bike #4'},
        ]

        self.ui.render_element_group(renderer=self.ui.render_text, group_name="bike_list_group", elements=bike_list)

        self.ui.render_button(element_name="checkout_button", text="Check Out")

        print(self.state.is_authenticated)

    def logout(self):
        self.state.is_authenticated = False
        self.go_to_view('welcome')