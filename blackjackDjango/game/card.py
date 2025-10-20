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

  def to_dict(self):
    return {"rank": self.rank, "suit": self.suit}

  # allows instantiation of objects from a given dictionary
  @classmethod
  def from_dict(cls, data):
    return cls(data["rank"], data["suit"])
