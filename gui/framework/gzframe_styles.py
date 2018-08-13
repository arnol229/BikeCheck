from framework.gzframe_utils import merge_two_dicts, with_callable, without_callable
class GZFrameStyles:
    def __init__(self, dictionary):
        self.__layout = 'vertical'

    def set_layout(self, layout):
        self.__layout = layout