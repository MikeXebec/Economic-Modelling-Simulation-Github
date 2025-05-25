# Session 14


import random

SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in SUITS for v in VALUES]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, count=5):
        return [self.cards.pop() for _ in range(count)]

class PokerHand:
    def __init__(self, cards):
        self.cards = cards
        self.suits = [card.suit for card in cards]
        self.values = [card.value for card in cards]

    def _value_counts(self):
        counts = {}
        for val in self.values:
            counts[val] = counts.get(val, 0) + 1
        return list(counts.values())

    def evaluate(self):
        counts = self._value_counts()
        if all(s == self.suits[0] for s in self.suits):
            return "Flush"
        elif 4 in counts:
            return "Four of a Kind"
        elif 3 in counts:
            return "Three of a Kind"
        elif counts.count(2) == 2:
            return "Two Pair"
        elif 2 in counts:
            return "Pair"
        else:
            return "High Card"

    def show(self):
        return ", ".join(str(card) for card in self.cards)

class PokerGame:
    def __init__(self, player_names):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = {name: PokerHand(self.deck.deal()) for name in player_names}

    def play(self):
        print("\n=== Poker Results ===")
        for name, hand in self.players.items():
            print(f"{name}: {hand.show()} -> {hand.evaluate()}")

if __name__ == '__main__':
    PokerGame(["Neo", "Trinity", "Morpheus"]).play()