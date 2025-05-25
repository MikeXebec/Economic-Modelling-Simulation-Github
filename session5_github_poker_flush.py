# Session 5

import random

SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in SUITS for value in VALUES]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_hand(self, size=5):
        return [self.cards.pop() for _ in range(size)]

class PokerHand:
    def __init__(self, cards):
        self.cards = cards

    def show(self):
        return ", ".join(str(card) for card in self.cards)

    def is_flush(self):
        suits = [card.suit for card in self.cards]
        return all(suit == suits[0] for suit in suits)

    def count_values(self):
        counts = {}
        for card in self.cards:
            counts[card.value] = counts.get(card.value, 0) + 1
        return counts

    def has_pair(self):
        return 2 in self.count_values().values()

    def has_three_of_a_kind(self):
        return 3 in self.count_values().values()

    def evaluate(self):
        if self.is_flush():
            return "Flush"
        elif self.has_three_of_a_kind():
            return "Three of a Kind"
        elif self.has_pair():
            return "Pair"
        else:
            return "High Card"

def play_round():
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck.deal_hand())

    print("Your hand:")
    print(hand.show())
    print("\nHand Type:", hand.evaluate())

if __name__ == '__main__':
    play_round()