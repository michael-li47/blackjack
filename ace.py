from card import Card

class Ace:
    def __init__(self, suit):
        super(Ace, self).__init__("Ace", suit)
        self.value = 1
    
    def blackjackValue(self, hand):
        handValue = hand.getDeckValue()
        
        