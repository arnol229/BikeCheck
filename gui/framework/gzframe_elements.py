class GZFrameElement:
    count = 0
    def __init__(self, element_name, element_type = None, element_props = {}, parent_name = None, element = None, index=0):
        self.element_name = element_name
        self.element_type = element_type
        self.element_props = element_props
        self.parent_name = parent_name
        self.element = element
        self.index = index
        self.id = 'gzframe_element_' + str(self.count)
        self.count = self.count + 1

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