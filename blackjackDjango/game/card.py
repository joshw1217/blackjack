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
      return [1, 11]
    elif self.rank in ["K", "Q", "J"]:
      return [10]
    else:
      return [int(self.rank)]

  def to_dict(self):
    return {"rank": self.rank, "suit": self.suit}

  @classmethod
  def from_dict(cls, data):
    return cls(data["rank"], data["suit"])
