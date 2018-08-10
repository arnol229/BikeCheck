from framework.gzframe_utils import merge_two_dicts

class GZFrameProps:
    def __init__(self, dictionary):
        merged_dict = merge_two_dicts(vars(self), dictionary)
        for k, v in merged_dict.items():
            setattr(self, k, v)

    def get_dict(self):
        return vars(self)