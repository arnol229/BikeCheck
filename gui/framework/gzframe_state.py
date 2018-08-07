class GZFrameState:
    def __init__(self, dictionary):
        self.update_state(dictionary)

    def update_state(self, dictionary):
        merged_dict = self.merge_two_dicts(vars(self), dictionary)
        for k, v in merged_dict.items():
            setattr(self, k, v)

    def merge_two_dicts(self, x, y):
        z = x.copy()   # start with x's keys and values
        z.update(y)    # modifies z with y's keys and values & returns None
        return z
        
