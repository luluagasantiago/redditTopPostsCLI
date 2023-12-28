from asciimatics.screen import Screen
from asciimatics.widgets import Frame, ListBox, Layout, Widget, Text
from asciimatics.scene import Scene





def demo(screen):
    dim = screen.dimensions
    
    # a frame belongs to a screen and it has layouts
    frame = Frame(screen, dim[0], dim[1])
    

    layout = Layout([100], fill_frame=True)
    frame.add_layout(layout)
    

    # A layout has widgets
    layout.add_widget(Text("Name:", "name"))
    

    # this is necessary
    effects = [frame]


    #This displays
    screen.play([Scene(effects, 500)])

Screen.wrapper(demo)

