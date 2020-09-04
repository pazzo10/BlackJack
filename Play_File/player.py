import sys
sys.path.append("/Users/paola/DEV PYTHON/PROJETS/BlackJack/BlackJack/Ascii_File")
from Ascii_File.ascii import Ascii

class Player:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)
    
    def sum_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "ACE":
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10

        if has_ace and self.value > 21:
            self.value -= 10

    def result(self):
        self.sum_value()
        return self.value
    
    def show(self):
        if self.dealer:
            print("UNREVEALED")
            print(self.cards[1])
        else:
            for card in self.cards:
                print(card)
            print("The total is:", self.result())


