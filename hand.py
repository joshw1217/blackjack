from card import Card

class Hand:
  def __init__(self):
    self.cards = []
    self.value = 0

  def __str__(self):
    return f"Hand of {len(self.cards)} cards, cards are: {self.cards} with value of {self.value}"
  
  def __repr__(self):
    return f"Hand(cards={self.cards}, value={self.value})"

  def add_card(self, card):
    self.cards.append(card)
    self.value += card.value()

  def evaluate(self):
    if(self.value > 21):
      return "Bust"
    elif(self.value == 21):
      return "Blackjack"
    else:
      return f"Value is {self.value}"