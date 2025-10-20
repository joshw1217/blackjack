from .card import Card

class Hand:
  def __init__(self):
    self.cards = []

  def __str__(self):
    return f"Hand of {len(self.cards)} cards, cards are: {self.cards} with value of {self.value}"
  
  def __repr__(self):
    return f"Hand(cards={self.cards}, value={self.value})"

  def add_card(self, card):
    self.cards.append(card)
  
  # Acts as a class attribute, computes "true" value by accounting for aces and if those aces would the hand bust
  @property
  def value(self):
    total = 0
    aces = 0
    for card in self.cards:
      if card.rank == "A":
        total += 11
        aces += 1
      elif card.rank in ["K", "Q", "J"]:
        total += 10
      else:
        total += int(card.rank)
    while total > 21 and aces:
      total -= 10
      aces -= 1
    return total


  def evaluate(self):
    if(self.value > 21):
      return "Bust"
    elif(self.value == 21 and len(self.cards) == 2):
      return "Blackjack"
    else:
      return self.value
