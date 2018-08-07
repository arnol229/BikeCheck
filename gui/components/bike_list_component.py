from framework.gzframe_component import GZFrameComponent
from framework.gzframe_elements import GZFrameButton, GZFrameText, GZFrameContainer

class BikeListComponent(GZFrameComponent):
    def __init__(self, element_name, state={}, props={}):
        super().__init__(element_name, state=state, props=props)

    def create_list(self, current_list):
        bike_list = []
        for x in range(0, len(current_list)):
            num = str(x)
            bike_list.append(
                GZFrameContainer(element_name=("bike_item_group_" + num), children=[
                    GZFrameText(element_name=("bike_group_" + num), props={"text":current_list[x]['text'], "size":20, "font":"Times New Roman", "color":"black", "grid": [0,0]}),
                    GZFrameText(element_name=("bike_item_status_" + num), props={"text":current_list[x]['availability'], "size":20, "font":"Times New Roman", "color":"black", "grid": [1,0]})
                ], props={'layout': 'grid'})
            )
        return bike_list

    def render(self, state):
        return self.create_list(self.props['bike_list'])