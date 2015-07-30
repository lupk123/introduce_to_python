# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
playTime = 0
outcome = ""
score = 0
mark = 0
#flag = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cardList = []

    def __str__(self):
        ans = "Hand constains "
        for i in range(len(self.cardList)):
            ans += str(self.cardList[i])
            ans += " "
        return ans
    
    def add_card(self, card):
        self.cardList.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        count = 0
        mark = 0
        flag = 0
        for i in range(len(self.cardList)):
            if self.cardList[i].get_rank() == "A":
                count += 1
                mark = 1
            else:                
                count += VALUES[self.cardList[i].get_rank()]                
        if mark == 1 and count + 10 <= 21:
            count += 10
        return count
   
    def draw(self, canvas, pos):
        #CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank)
        # draw a hand on the canvas, use the draw method for cards          
        for i in range(len(self.cardList)):
            if i > 0:
                pos[0] += CARD_SIZE[0] + 20
            self.cardList[i].draw(canvas, pos)           
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                card = Card(SUITS[i], RANKS[j])
                self.deck.append(card)

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)
        return self.deck

    def deal_card(self):
        num = random.randrange(0, len(self.deck))
        return self.deck[num]
    
    def __str__(self):
        ans = ""
        for i in range(len(self.deck)):
            ans += str(self.deck[i])
        return ans   



#define event handlers for buttons
def deal():    
    global outcome, in_play	, dealer, player, deck, mark, playTime, score, flag   
    if in_play == True:
        score -= 1
    #shuffle the deck
    deck = Deck()
    deck.shuffle()
    dealer = Hand()
    player = Hand()
    #deale card to dealer and player
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
#    player.add_card(Card('S', 'A'))
#    player.add_card(Card('S', 'K'))
    outcome = ""
    in_play = True
    flag = 0
    playTime += 1    
#    print player.get_value()
#    if player.get_value() == 21:
#        outcome = "You win!!!"
#        in_play = False
#        score += 1

def hit(): 
    # if the hand is in play, hit the player
    global player, outcome, in_play, score, flag
    if in_play == True:
        player.add_card(deck.deal_card())
    # if busted, assign a message to outcome, update in_play and score
        if player.get_value() > 21:            
            outcome = "Bust!!! You lose!!!"
            in_play = False
            score -= 1
#            flag = 1
#        elif player.get_value() == 21:
#            outcome = "You win!!!"
#            in_play = False
#            score += 1
#            flag = 1        
        
def stand(): 
    global dealer, score, in_play, outcome, flag
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play == True:
        while dealer.get_value() <= 16:
            dealer.add_card(deck.deal_card()) 
#        flag = 1            
        in_play = False
        # assign a message to outcome, update in_play and score
        dealerValue = dealer.get_value()
        playerValue = player.get_value()
        if dealerValue > 21:
            outcome = "You Win!!!"
            score += 1        
        elif dealerValue >= playerValue:
            outcome = "You lose!!!"
            score -= 1 
        else:
            outcome = "You Win!!!"
            score += 1 
    
# draw handler    
def draw(canvas):
    global score, in_play
    canvas.draw_text("Blackjack", [50, 50], 40, "white")
    canvas.draw_text("dealer:", [50, 130], 30, "white")
    canvas.draw_text(outcome, [250, 130], 30, "white")
    canvas.draw_text("play time:"+str(playTime), [300, 50], 30, "white")
    canvas.draw_text("Score "+str(score), [470, 50], 30, "white")
    canvas.draw_text("player:", [50, 350], 30, "white")
#    canvas.draw_text("Hit or stand?", [250, 350], 30, "white")
    pos = [50, 150]	    
    dealer.draw(canvas, pos)
    #if flag == 0:
    if in_play == True:
        pos = [50, 150]
        canvas.draw_image(card_back, CARD_CENTER, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)    
        canvas.draw_text("Hit or stand?", [250, 350], 30, "white")
    else:            
        canvas.draw_text("New deal?", [250, 350], 30, "white")            
        
    pos = [50, 380]	
    player.draw(canvas, pos)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("#0080ff")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

# remember to review the gradic rubric
