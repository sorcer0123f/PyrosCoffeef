#imports modules that the game requires
import time, os, random

#values for the decks of cards
ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
suits = ["Clubs","Hearts","Diamonds","Spades"]
deck = []

#nested loop to add cards to suits and then to a list 'deck' and adds a higher value to each rank
value = 1
for rank in ranks:
    for suit in suits:
        deck.append([rank + " of " + suit, value])
    value = value + 1
    #shuffles the deck using the random module
random.shuffle(deck)
score = 0 #keeps track of score
card1 = deck.pop(0)