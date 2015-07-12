# implementation of card game - Memory

import simplegui
import random

cards = []
pre1_index = -1
pre2_index = -1
state = 0


# helper function to initialize globals
def new_game():
    global cards, pre1_index, pre2_index, exposed, Turns
    Turns = 0
    label.set_text("Turns = "+str(Turns))
    exposed = []
    cards = range(8) * 2
    random.shuffle(cards)
    for i in range(16):
        exposed.append(0);
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed, pre1_index, pre2_index, Turns
    temp = pos[0] // 50
    if exposed[temp] == 0:
        if state == 0:
            pre1_index = temp
            exposed[temp] = 1
            state = 1
        elif state == 1:
            pre2_index = temp
            exposed[temp] = 1
            state = 2
            Turns += 1
            label.set_text("Turns = "+str(Turns))
        else:
            if cards[pre1_index]!= cards[pre2_index]:
                exposed[pre1_index] = 0
                exposed[pre2_index] = 0                
            exposed[temp] = 1
            state = 1
            pre1_index = temp                                                      
        
#    if exposed[temp] == 0:
#        exposed[temp] = 1
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for card_index in range(len(cards)):
        card_pos = 50 * card_index
        if exposed[card_index] == 1:
            canvas.draw_text(str(cards[card_index]), [card_pos + 10, 60], 50, "white")
        else:                       
            canvas.draw_polygon([(card_pos + 50, 0), (card_pos, 0), (card_pos, 100), (card_pos+50, 100)], 1, "black", "green")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric