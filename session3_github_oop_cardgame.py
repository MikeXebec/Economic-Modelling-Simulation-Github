# Session 3

import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self):
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num):
        return [self.cards.pop() for _ in range(num)]

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_cards(self, cards):
        self.hand.extend(cards)

    def show_hand(self):
        return ", ".join(str(card) for card in self.hand)

def play_card_game():
    players = [Player("Alice"), Player("Bob")]
    deck = Deck()
    deck.shuffle()

    for player in players:
        player.receive_cards(deck.deal(5))
        print(f"\n{player.name}'s hand:")
        print(player.show_hand())

if __name__ == "__main__":
    play_card_game()