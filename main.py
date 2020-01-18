from deck import Deck
from card import Card
from blackjack import BlackJack

def reset():
    d = Deck(True)
    d.shuffleDeck()
    bj.__init__(d)
    bj.end = True

def hit():
    bj.dealPlayer()

def stay():
    bj.phase = "dealer"
    print("\n Dealer's Turn \n")

def dealer():
    bj.dealDealer()

def blackjack():
    bj.end = False
    bj.dealPlayer()
    while bj.end != True:
        if bj.phase == "player":
            player_choice = input("Hit or Stay?: ")
            if player_choice == "hit":
                hit()
            elif player_choice == "stay":
                stay()
            elif player_choice == "end":
                print("GAME OVER")
                bj.end = True
            elif player_choice == "start over":
                reset()
                blackjack()
            else:
                print("Invalid Input")
        else:
            dealer()
    
    if bj.end == True:
        play_again = input("Play Again?(y/n): ")
        if play_again == "y":
            reset()
            blackjack()
        elif play_again == "n":
            print("END")
            

d = Deck(True)
d.shuffleDeck()
bj = BlackJack(d)

if __name__ == "__main__":
    play = ""

    while play != "y":
        play = input("Play? (y/n): ")
    
    blackjack()