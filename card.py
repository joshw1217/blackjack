class Card:
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit

  def __str__(self):
    return f"{self.rank} of {self.suit}"

  def __repr__(self):
    return f"Card(rank='{self.rank}', suit='{self.suit}')"
  
  def __eq__(self, other):
    return self.rank == other.rank and self.suit == other.suit

  def value(self):
    if self.rank == "A":
      return 11
    elif self.rank in ["K", "Q", "J"]:
      return 10
    else:
      return int(self.rank)

card1 = Card("A", "Spades")
card2 = Card("Q", "Hearts")
card3 = Card("4", "Clubs")
card4 = Card("A", "Spades")

print(card1, card2, card3)
print(card1 == card4)