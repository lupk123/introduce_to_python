# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        number = 5
    return number

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name =  "scissors"
    else:
        name = "error input"
    return name
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    
import random
def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below    
    # print a blank line to separate consecutive games
    print "\n"
    # print out the message for the player's choice 
    print "Player chooses "+player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    computer = random.randint(0, 4)    
    
    # convert comp_number to comp_choice using the function number_to_name()
    computer_choice = number_to_name(computer)    
    
    # print out the message for computer's choice
    print "Computer chooses "+computer_choice
    
    # compute difference of comp_number and player_number modulo five
    modulo = (player - computer) % 5
    
    # use if/elif/else to determine winner, print winner message
    if modulo == 0:
        print "Player and computer tie!"
    elif (modulo == 1) or (modulo == 2):
        print "Player wins!"
    elif (modulo == 3) or (modulo == 4):
        print "Computer wins!"
    else:
        print "error...."   

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


