from deck import Deck
from hand import Hand

deck = Deck()
hand = Hand()
hand.add_card(deck.draw())
hand.add_card(deck.draw())

proceed = True
while(proceed):
  bust = False
  while(1):
    print(hand)
    print("Would you like to 1.hit or 2.stand?")
    choice = input()
    if(choice == "hit" or choice == "1"):
      hand.add_card(deck.draw())
      print(hand)
      if(hand.evaluate() == "Bust"):
        print(f"You bust!, hand value is {hand.value}")
        bust = True
        break
      elif(hand.evaluate() == "Blackjack!"):
        print("You got Blackjack!")
        break
      else:
        print(f"Hand value is {hand.value}")
    if(choice == "stand" or choice == "2"):
      print(f"You stand with hand value of {hand.value}")
      break
  if(bust):
    print("You lost because you busted!")
  else:
    dealer_hand = Hand()
    dealer_hand.add_card(deck.draw())
    dealer_hand.add_card(deck.draw())
    print(dealer_hand)
    print(dealer_hand.evaluate())
    while(dealer_hand.value < 17):
      dealer_hand.add_card(deck.draw())
      print(dealer_hand)
      print(dealer_hand.evaluate())
      if(dealer_hand.evaluate() == "Bust"):
        print("Dealer bust!") # TODO: Player still loses if dealer busts
        break
      elif(dealer_hand.evaluate() == "Blackjack!"):
        print("Dealer got Blackjack!")
        break
      else:
        print(f"Dealer hand value is {dealer_hand.value}")

    if(hand.value > dealer_hand.value):
      print("You win!")
    elif(hand.value < dealer_hand.value):
      print("You lose!")
    else:
      print("Push!")

    print("Would you like to play again? yes or 1 to proceed")
    choice = input()
    if(choice == "yes" or choice == "1"):
      proceed = True
    else:
      proceed = False

# TODO: Finish writing this up and implement above ^^
def evaluateGameState(playerHand: Hand, dealerHand: Hand):
  if(playerHand.evaluate() == "Bust"):
    print(f"Player busts with value of {playerHand.value}!")
  elif(playerHand.evaluate() == "Blackjack"):
    print("Player wins with a blackjack!")
  elif(playerHand > dealerHand):
    print(f"Your hand value of {playerHand.value} beats the dealer's hand of {dealerHand.value}!")
  elif(playerHand.value == dealerHand.value):
    print("Push!")
  else:
    print(f"Dealer's hand of value {dealerHand.value}")
  
  