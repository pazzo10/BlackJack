from random import shuffle
import sys
sys.path.append("/home/patrick/Desktop/Draft/BlackJack/")
from Card_File.card import Card


class Deck:
    def __init__(self):
        self.cards = [Card(c, v) for c in ["♥", "♦", "♣",
                      "♠"] for v in ["ACE", "2", "3", "4", "5", "6",
                      "7", "8", "9", "10", "J", "Q", "K"]]
 
    def shuffle(self):
        if len(self.cards) > 1:
            shuffle(self.cards)
 
    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

