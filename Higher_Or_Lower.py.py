#imports modules that the game requires
import blessed, time, random

#instatiates the blessed terminal
term = blessed.Terminal()

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

def print_card():
    print(term.violetred1+ '''
 ------------- 
|J            |
|O  -------   |
|K |       |  |
|E | J     |  |
|R |  O    |  |
|  |   K   |  |
|  |    E  | J|
|  |     R | O|
|  |       | K|
|   -------  E|
|            R|
 ------------- 
        ''')

while True:
    #start of the game
    print(term.clear)
    print_card()
    print(term.blue+ "Your score so far is", score)
    print(term.pink+ "\n\nThe current card is", card1[0])
    while True:
        choice = input(term.gold+ "higher or lower?")
        if len(choice) > 0:
            if choice[0].lower() in ["h","l"]:
                break
        
    #selects the next card
    card2 = deck.pop(0)
    print(term.pink+ "The next card picked is", card2[0])
    time.sleep(1)

    #determines if the player's choice is correct or not
    if choice[0].lower() == "h" and card2[1] > card1[1]:
        print(term.green3+ "Correct!")
        score +=1
        time.sleep(1)
    if choice[0].lower() == "h" and card2[1] < card1[1]:
        print(term.orangered+ "Wrong!")
        time.sleep(1)
        break
    if choice[0].lower() == "l" and card2[1] < card1[1]:
        print(term.green3+ "Correct!")
        score +=1
        time.sleep(1)
    if choice[0].lower() == "l" and card2[1] > card1[1]:
        print(term.orangered+ "Wrong!")
        time.sleep(1)
        break
    else:
        print(term.darkmagenta+ "draw!" + term.normal)

    card1 = card2

    #game ends and displays your final score before terminating
print(term.clear)
print(term.red3+ "Game over!")
print(term.blue + "Your final score is", score)
time.sleep(4)
print(term.clear)