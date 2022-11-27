import logging
from PokerGame.models.deck import Deck
from PokerGame.models.hand import Hand

_logger = logging.getLogger(__name__)


class Match:

	deck = Deck()

	def __init__(self):
		self.deck.shuffle()
		self.player1 = Hand(self.deck.give_cards(5))
		self.player2 = Hand(self.deck.give_cards(5))
		self.player3 = Hand(self.deck.give_cards(5))
		self.player4 = Hand(self.deck.give_cards(5))
		self.player5 = Hand(self.deck.give_cards(5))

	def ask_change_cards(self, hand_player, index_number_of_card):
		hand_player.replace_cards(index_number_of_card, self.deck.give_cards(len(index_number_of_card)))

	def __str__(self):
		print("Player1 cards: ")
		self.player1.__str__()
		print("Player1 point: " + str(self.player1.compute_score()))
		self.player1.compute_score()
		print("Player2 cards: ")
		self.player2.__str__()
		print("Player2 point: " + str(self.player2.compute_score()))
		print("Player3 cards: ")
		self.player3.__str__()
		print("Player3 point: " + str(self.player3.compute_score()))
		print("Player4 cards: ")
		self.player4.__str__()
		print("Player4 point: " + str(self.player4.compute_score()))
		print("Player5 cards: ")
		self.player5.__str__()
		print("Player5 point: " + str(self.player5.compute_score()))

	def match_winner(self):
		return max(self.player1.compute_score(), self.player2.compute_score(), self.player3.compute_score(), self.player4.compute_score(), self.player5.compute_score())




