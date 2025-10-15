from deck import Deck
from hand import Hand

deck = Deck()
hand = Hand()
hand.add_card(deck.draw())
hand.add_card(deck.draw())
print(hand)
print(hand.evaluate())