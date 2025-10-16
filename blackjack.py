from deck import Deck
from hand import Hand
from card import Card

# Function playing a round and determining if the game should end
def playRound(player: Hand, deck: Deck):
  print(f"Player hand is {player.cards} valued at {player.value}")
  if(player.evaluate() == "Blackjack"):
    return player, deck, False
  choice = input("Would you like to 1. Hit or 2. Stay?")
  if(choice.lower() == "hit" or choice == "1"):
    drawnCard = deck.draw()
    player.add_card(drawnCard)
    print(f"Player draws a {drawnCard}, putting you at {player.value}")
    if(player.evaluate() == "Bust"):
      print(f"Player busts with value of {player.value}!")
      return player, deck, False
  if(choice.lower() == "stay" or choice == "2"):
    return player, deck, False
  return player, deck, True

# Function for playing the dealer's hand, determining if dealer busts
def playDealer(dealer: Hand, deck: Deck):
  while(dealer.value < 17):
    drawnCard = deck.draw()
    dealer.add_card(drawnCard)
    print(f"Dealer draws a {drawnCard}, new hand value is {dealer.value}")
  if(dealer.evaluate() == "Bust"):
    return dealer, deck, True
  return dealer, deck, False

# Goes when player is done drawing, plays dealer out and then determines winner
def showdown(player: Hand, dealer: Hand, deck: Deck):
  print(f"Dealer flips face down card, revealing a {dealer.cards[1]}, hand value is {dealer.value}")
  if(player.evaluate() == "Blackjack"):
    if(dealer.evaluate() == "Blackjack"):
      print("Player and Dealer push on blackjack!")
    else:
      print("Player wins with Blackjack!")

  elif(player.evaluate() == "Bust"):
    print(f"Player loses after busting with value of {player.value}")

  else:
    dealer, deck, dealerBust = playDealer(dealer, deck)
    if(dealerBust):
      print("Dealer bust! Player wins!")
    elif(player.value > dealer.value):
      print(f"Player hand of {player.value} beats dealer hand of {dealer.value}!")
    elif(player.value < dealer.value):
      print(f"Player hand of {player.value} loses to dealer hand of {dealer.value}!")
    elif(player.value == dealer.value):
      print("Push!")



# Prepare initial deck and betting balance
deck = Deck()


# Loop until player is finished playing
proceed = True
while(proceed):
  if(len(deck.cards) < 18):
    print("Deck low on cards... Reshuffling...")
    deck.reshuffle()


  
  player = Hand()
  player.add_card(deck.draw())
  player.add_card(deck.draw())
  # player.add_card(Card("A", "Spades"))
  # player.add_card(Card("K", "Diamonds"))

  dealer = Hand()
  # dealer.add_card(Card("A", "Spades"))
  # dealer.add_card(Card("K", "Diamonds"))
  dealer.add_card(deck.draw())
  dealer.add_card(deck.draw())
  anotherRound = True

  print(f"Dealer hand is {dealer.cards[0]} with value of {dealer.hiddenValue()}. One card is face down.")

  # Run a blackjack round as a player
  while(anotherRound):
    player, deck, anotherRound = playRound(player, deck)
  
  outcome = showdown(player, dealer, deck)

  choice = input("Would you like to play again? yes or 1 to proceed")
  if(choice == "yes" or choice == "1"):
    proceed = True
  else:
    proceed = False

  
  