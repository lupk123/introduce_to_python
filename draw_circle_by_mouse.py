# Examples of mouse input

import simplegui
import math

width = 400
height = 300
position = [width/2, height/2]
ball_color = 'red'
radious = 20

def distance(pos):
    return math.sqrt((pos[0] - position[0]) ** 2 + (pos[1] - position[1]) ** 2)

def mouse_handler(pos):
    global position, ball_color
    dis = distance(pos)
    #print dis
    if(dis > radious):
        position = list(pos)
        ball_color = "red"
    elif(dis <= radious):
        if(ball_color == "red"):
            ball_color = "green"
        else:
            ball_color = "red"
    
def draw_handler(canvas):
    canvas.draw_circle(position, radious, 1, 'black', ball_color)

frame = simplegui.create_frame("Mouse click", width, height)
frame.set_canvas_background('white')
frame.set_mouseclick_handler(mouse_handler)
frame.set_draw_handler(draw_handler)

frame.start();