from framework.gzframe_utils import merge_two_dicts, with_callable, without_callable
class GZFrameElement:
    count = 0
    def __init__(self, element_name, element_type = None, props = {}, parent = None, element = None, index=0):
        self.element_name = element_name
        self.element_type = element_type
        self.props = self.create_props(props)
        self.parent = parent
        self.parent_name = ''
        self.parent_chain = ''
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
    def __init__(self, bg='white', width=None, children = [], *args, **kwargs):
        super().__init__(element_type = 'box', *args, **kwargs)
        self.bg = bg
        self.width = width
        self.children = children

class GZFrameText(GZFrameElement):
    def __init__(self, *args, **kwargs):
        super().__init__(element_type = 'text', *args, **kwargs)

class GZFrameButton(GZFrameElement):
    def __init__(self, on_click = None, *args, **kwargs):
        super().__init__(element_type = 'button', *args, **kwargs)
        self.on_click = on_click

class GZFramePicture(GZFrameElement):
    def __init__(self, height=50, width=50, *args, **kwargs):
        super().__init__(element_type = 'picture', *args, **kwargs)
        self.height = height
        self.width = width

    # def show(self):
    #     print(dir(self))
    #     self.element.show()