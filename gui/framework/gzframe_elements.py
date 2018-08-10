from framework.gzframe_utils import merge_two_dicts, with_callable, without_callable
class GZFrameElement:
    count = 0
    def __init__(self, element_name, element_type = None, props = {}, parent_name = None, element = None, index=0):
        self.element_name = element_name
        self.element_type = element_type
        self.props = self.create_props(props)
        self.parent_name = parent_name
        self.element = element
        self.index = index
        self.id = self.create_id()
        GZFrameElement.count += 1

    @classmethod
    def create_id(cls):
        return 'gzframe_element_' + str(cls.count)

    @classmethod
    def reset_count(cls):
        cls.count = 0

    def create_props(self, props):
        return merge_two_dicts(with_callable(props), without_callable(props))

class GZFrameContainer(GZFrameElement):
    def __init__(self, children = [], *args, **kwargs):
        super().__init__(element_type = 'box', *args, **kwargs)
        self.children = children

class GZFrameText(GZFrameElement):
    def __init__(self, *args, **kwargs):
        super().__init__(element_type = 'text', *args, **kwargs)

class GZFrameButton(GZFrameElement):
    def __init__(self, on_click = None, *args, **kwargs):
        super().__init__(element_type = 'button', *args, **kwargs)
        self.on_click = on_click