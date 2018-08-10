from framework.gzframe_utils import merge_two_dicts

class GZFrameState:
    def __init__(self, dictionary):
        self.update_state(dictionary)

    def update_state(self, dictionary):
        merged_dict = merge_two_dicts(vars(self), dictionary)
        for k, v in merged_dict.items():
            setattr(self, k, v)
        
