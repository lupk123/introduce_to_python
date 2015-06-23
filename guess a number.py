# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui

# initialize global variables used in your code here
num_range = 100
count = 7

# helper function to start and restart the game
def new_game():  
    global secret_number, count, num_range
    print "New game.	Range is from 0 to ", num_range
    print "Number of remaining guesses is ", count    
    secret_number = random.randrange(1, num_range)   
    print " "
       
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range, count
    count = 7
    num_range = 100    
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range, count
    count = 10
    num_range = 1000    
    new_game()
        
def input_guess(guess):
    # main game logic goes here	
    global count, num_range 
    count = count - 1
    guess = int(guess)
    start = 0;
    print "Guess was ",guess
    print "Number of remaining guesses is ",count  
    if(count >= 0):     	
        if(guess < secret_number):
            print "Higher!"            
            print " "
        elif(guess > secret_number):
            print "Lower!"
            print " "
        elif(guess == secret_number):
            print "Correct!"
            print " "            
            start = 1
    else:
        print "Out of guesses.	The number is", secret_number
        print " "
        start = 1
    if(start == 1):
        range100()            
    
# create frame
frame = simplegui.create_frame('Guess the Number', 200, 200)

# register event handlers for control elements and start frame
frame.add_button('Range: [0 - 100)', range100, 200)
frame.add_button('Range: [0 - 1000)',range1000, 200)
frame.add_input('Enter a guess', input_guess, 200)
 
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
