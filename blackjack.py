from deck import Deck
class BlackJack(Deck):

    def __init__(self, deck):
        self.player = Deck(False)
        self.playerSum = 0
        self.dealer = Deck(False)
        self.dealerSum = 0
        self.phase = "player"
        self.end = False
        self.deck = deck


    def addAcesPlayer(self, sum):
        if self.playerSum + 10 > 21:
            self.playerSum += 1
        else:
            self.playerSum += 10

    def addAcesDealer(self, sum):
        if self.dealerSum + 10 > 21:
            self.dealerSum += 1
        else:
            self.dealerSum += 10

    #Add aces thing
    def checkPlayerSum(self):
        self.playerSum = 0
        num_aces = 0
        for card in self.player.cards:
            if card.rank != 'Ace':
                self.playerSum += card.cardValue()
            else:
                self.playerSum += card.cardValue()[0]
                num_aces += 1     
        

    def dealPlayer(self):
        top_card = self.deck.dealCard()
        self.player.addCard(top_card)
        self.checkPlayerSum()
        print("Card: " + top_card.rank + " of " + top_card.suit)
        print("Currently at: " + str(self.playerSum) + "\n")
        if self.playerSum > 21:
            print("Bust . . . ")
            self.end = True
        else:
            pass

    #Add aces thing
    def checkDealerSum(self):
        self.dealerSum = 0
        num_aces = 0
        for card in self.dealer.cards:
            if card.rank != 'Ace':
                self.dealerSum += card.cardValue()
            else:
                self.dealerSum += card.cardValue()[0]
                num_aces += 1     
        

    def dealDealer(self):
        top_card = self.deck.dealCard()

        self.dealer.addCard(top_card)
        self.checkDealerSum()

        print("Card: " + top_card.rank + " of " + top_card.suit)
        print("Currently at: " + str(self.dealerSum) + "\n")
        
        if self.dealerSum > 21:
            print("Bust! Player Wins!")
            self.end = True
        elif self.dealerSum > self.playerSum:
            print("Dealer Wins.")
            self.end = True
        else:
            pass

    
