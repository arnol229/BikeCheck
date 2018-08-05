from guizero import Text, TextBox, PushButton, Slider, Picture, Box

class GZFrameCore:
    gui_classes = [Text, TextBox, PushButton, Slider, Picture, Box]
    def __init__(self, app):
        self.app = app

    def update_current_view(self, bikecheck, view_config, current_view, current_view_name):
        self.destroy_current_view(current_view)
        return view_config['name'], view_config['view'](bikecheck)

    def destroy_current_view(self, current_view):
        view_attrs = current_view.__dict__
        for attr in view_attrs:
            print(attr)
            for g_class in self.gui_classes:
                class_attr = getattr(current_view, attr)
                if isinstance(class_attr, g_class):
                    class_attr.destroy()
        current_view.ui.container.destroy()
