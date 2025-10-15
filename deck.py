from card import Card
import random

class Deck:
  suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
  ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

  def __init__(self):
    self.cards = self._create_deck()
    self.shuffle()

  def __str__(self):
    return f"Deck of {len(self.cards)} cards"

  def __repr__(self):
    return f"Deck(cards={self.cards})"

  def _create_deck(self):
    cards = []
    for suit in self.suits:
      for rank in self.ranks:
        cards.append(Card(rank, suit))
    return cards
  
  def shuffle(self):
    random.shuffle(self.cards)

  def reshuffle(self):
    self.cards = self._create_deck()
    self.shuffle()

  def draw(self):
    return self.cards.pop()
