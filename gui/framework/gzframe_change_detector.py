class GZFrameChangeDetector:
    def __init__(self, app, view, state):
        self.app = app
        self.old_state = vars(state)
        # self.app.repeat(300, self.check_changes)

    def check_changes(self):
        print('check')
