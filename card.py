class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = {'Ace': (1, 10), 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10,'King': 10}
    
    def showCard(self):
        print(self.rank + " of " + self.suit)
    
    def cardValue(self):
        return self.value[self.rank]
    
