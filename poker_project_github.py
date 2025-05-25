# Final Project Poker Logic Module


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
        self.cards = [Card(suit, val) for suit in SUITS for val in VALUES]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n=5):
        return [self.cards.pop() for _ in range(n)]

class PokerHand:
    def __init__(self, cards):
        self.cards = cards
        self.values = [card.value for card in cards]
        self.suits = [card.suit for card in cards]

    def show(self):
        return ", ".join(str(card) for card in self.cards)

    def evaluate(self):
        counts = self._value_counts()
        flush = all(s == self.suits[0] for s in self.suits)

        if flush:
            return "Flush"
        elif 4 in counts:
            return "Four of a Kind"
        elif 3 in counts:
            return "Three of a Kind"
        elif list(counts).count(2) == 2:
            return "Two Pair"
        elif 2 in counts:
            return "Pair"
        else:
            return "High Card"

    def _value_counts(self):
        counts = {}
        for v in self.values:
            counts[v] = counts.get(v, 0) + 1
        return list(counts.values())

class PokerGame:
    def __init__(self, players):
        self.deck = Deck()
        self.deck.shuffle()
        self.hands = {player: PokerHand(self.deck.deal()) for player in players}

    def play(self):
        print("\n--- Final Poker Game Simulation ---")
        for player, hand in self.hands.items():
            print(f"{player}: {hand.show()} --> {hand.evaluate()}")

if __name__ == '__main__':
    players = ["Alice", "Bob", "Charlie"]
    game = PokerGame(players)
    game.play()