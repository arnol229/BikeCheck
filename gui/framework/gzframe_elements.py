class GZFrameElement:
    count = 0
    def __init__(self, element_name, element_type = None, element_props = {}, parent_name = None, element = None, index=0):
        self.element_name = element_name
        self.element_type = element_type
        self.element_props = self.create_props(element_props)
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

    def create_props(self, element_props):
        return self.merge_two_dicts(self.without_callable(element_props), self.with_callable(element_props))

    def merge_two_dicts(self, x, y):
        z = x.copy()   # start with x's keys and values
        z.update(y)    # modifies z with y's keys and values & returns None
        return z

    def without_callable(self, props):
        return {x: props[x] for x in props if not callable(props[x])}

    def with_callable(self, props):
        return {x: props[x] for x in props if callable(props[x])}

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