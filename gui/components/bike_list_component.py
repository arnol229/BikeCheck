from framework.gzframe_component import GZFrameComponent
from framework.gzframe_elements import GZFrameButton, GZFrameText, GZFrameContainer

class BikeListComponent(GZFrameComponent):
    def __init__(self, element_name, state={}, element_props={}):
        super().__init__(element_name, state=state, element_props=element_props)

    def create_list(self, current_list):
        bike_list = []
        for x in range(0, len(current_list)):
            num = str(x)
            bike_list.append(
                GZFrameContainer(element_name=("bike_item_group_" + num), children=[
                    GZFrameText(element_name=("bike_group_" + num), element_props={"text":current_list[x]['text'], "size":20, "font":"Times New Roman", "color":"black", "grid": [0,0]}),
                    GZFrameText(element_name=("bike_item_status_" + num), element_props={"text":current_list[x]['availability'], "size":20, "font":"Times New Roman", "color":"black", "grid": [1,0]})
                ], element_props={'layout': 'grid'})
            )
        return bike_list

    def render(self, props, state):
        return self.create_list(props['bike_list'])