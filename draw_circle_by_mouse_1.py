# Examples of mouse input

import simplegui
import math

width = 400
height = 300
position_list = []
radious = 15
ball_color = "red"

def distance(pos, position):
    return math.sqrt((pos[0] - position[0]) ** 2 + (pos[1] - position[1]) ** 2)

def mouse_handler(pos):
    changed = False
    global position_list, ball_color

    remove = []
    for position in position_list:
        dis = distance(pos, position)   
        if(dis <= radious):
            remove.append(position)
#            position_list.remove(position)
#            changed = True;
#            if(position[2] == "red"):
#                position[2] = "green"
#            else:
#                position[2] = "red"    
    
    if remove == []:        
        position_list.append(pos)  
    else:
        for ball in remove:
            position_list.pop(position_list.index(ball))
    
def draw_handler(canvas):
    for position in position_list:
        canvas.draw_circle([position[0], position[1]], radious, 1, 'black', ball_color)

frame = simplegui.create_frame("Mouse click", width, height)
frame.set_canvas_background('white')
frame.set_mouseclick_handler(mouse_handler)
frame.set_draw_handler(draw_handler)

frame.start();