from card import Card

class Deck(object):
    
    def __init__(self, full):
        self.cards = []
        if full == True:
            self.addDeck()
        else:
            pass

    def addDeck(self):
        ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen','King']
        suits = ['Hearts', 'Diamonds', 'Spaids', 'Clubs']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
    
    def emptyDeck(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def shuffleDeck(self):
        from random import shuffle
        shuffle(self.cards)
    
    def getDeckSize(self):
        return len(self.cards)

    def showDeck(self):
        for card in self.cards:
            card.showCard()
    
    def topCard(self):
        top = self.cards[0]
        return top

    def newDeck(self):
        self.cards = []
        self.addDeck()

    def dealCard(self):
        return self.cards.pop(0)
        
        
        