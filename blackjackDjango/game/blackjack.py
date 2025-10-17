from .deck import Deck
from .hand import Hand
from .card import Card


class BlackjackGame:
    def __init__(self, balance=1000):
        self.balance = balance
        self.bet = 0
        self.deck = Deck()
        self.player = Hand()
        self.dealer = Hand()
        self.round_active = False
        self.message = ""

    # --- Round Management ---

    def start_round(self, bet: int):
        """Start a new round and deal cards"""
        if self.round_active:
            return  # don’t start a new one mid-round
        self.bet = bet
        self.round_active = True
        self.message = ""
        self.player = Hand()
        self.dealer = Hand()

        # reshuffle deck if it’s low
        if len(self.deck.cards) < 10:
            self.deck.reshuffle()

        # deal opening hands
        self.player.add_card(self.deck.draw())
        self.player.add_card(self.deck.draw())
        self.dealer.add_card(self.deck.draw())
        self.dealer.add_card(self.deck.draw())

        # check for blackjack
        if self.player.evaluate() == "Blackjack":
            self.round_active = False
            self.balance += int(bet * 1.5)
            self.message = "Player wins with Blackjack!"

    # --- Player Actions ---

    def player_hit(self):
        if not self.round_active:
            return
        self.player.add_card(self.deck.draw())
        if self.player.evaluate() == "Bust":
            self.round_active = False
            self.balance -= self.bet
            self.message = f"Player busts with value {self.player.value}."

    def player_stay(self):
        if not self.round_active:
            return
        self.play_dealer()
        self.determine_winner()

    def player_double_down(self):
        if not self.round_active or self.bet * 2 > self.balance:
            return
        self.bet *= 2
        self.player.add_card(self.deck.draw())
        if self.player.evaluate() == "Bust":
            self.round_active = False
            self.balance -= self.bet
            self.message = "Player busts after doubling down."
        else:
            self.play_dealer()
            self.determine_winner()

    # --- Dealer Logic ---

    def play_dealer(self):
        while self.dealer.value < 17:
            self.dealer.add_card(self.deck.draw())

    def determine_winner(self):
        """Compare player/dealer hands and settle balance."""
        self.round_active = False
        if self.dealer.evaluate() == "Bust":
            self.balance += self.bet
            self.message = f"Dealer busts! Player wins {self.bet}."
        elif self.player.value > self.dealer.value:
            self.balance += self.bet
            self.message = f"Player wins with {self.player.value} over dealer's {self.dealer.value}."
        elif self.player.value < self.dealer.value:
            self.balance -= self.bet
            self.message = f"Dealer wins with {self.dealer.value} over {self.player.value}."
        else:
            self.message = "Push! No winner."

    # --- Serialization Helpers ---

    def to_dict(self):
        """Convert current state to a JSON-serializable dict."""
        return {
            "balance": self.balance,
            "bet": self.bet,
            "deck": [card.to_dict() for card in self.deck.cards],
            "player": [card.to_dict() for card in self.player.cards],
            "dealer": [card.to_dict() for card in self.dealer.cards],
            "round_active": self.round_active,
            "message": self.message,
        }

    @classmethod
    def from_dict(cls, data):
        game = cls(balance=data.get("balance", 1000))
        game.bet = data.get("bet", 0)
        game.round_active = data.get("round_active", False)
        game.message = data.get("message", "")
        game.deck.cards = [Card.from_dict(c) for c in data.get("deck", [])]
        game.player.cards = [Card.from_dict(c) for c in data.get("player", [])]
        game.dealer.cards = [Card.from_dict(c) for c in data.get("dealer", [])]
        return game
