class GZFrameState:
    def __init__(self):
        self.is_authenticated = False
        self.auth_token = None
        self.user_id = None
        self.name = None
        self.is_back_enabled = True