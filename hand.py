from card import Card

class Hand:
  def __init__(self):
    self.cards = []
    self.value = 0

  def __str__(self):
    return f"Hand of {len(self.cards)} cards, cards are: {self.cards}"
  
  def __repr__(self):
    return f"Hand(cards={self.cards})"

  def add_card(self, card):
    self.cards.append(card)
    self.value += card.value()

  def get_value(self):
    return self.value

  def evaluate(self):
    if(self.value > 21):
      return f"Bust, value is {self.value}"
    elif(self.value == 21):
      return "Blackjack!"
    else:
      return f"Value is {self.value}"