import logging
import random
from PokerGame.models.card import Card
_logger = logging.getLogger(__name__)


class Deck:
	"""Linear structure of 52 distinct cards"""
	deck_cards = []

	def __init__(self):
		for seed in range(1, 5):
			for value in range(1, 14):
				self.deck_cards.append(Card(value, seed))

	def shuffle(self):
		return random.shuffle(self.deck_cards)

	def give_cards(self, card_number):
		if card_number < 1 or card_number > 5:
			print("Enter a valid number: 1 <= n <= 5 ")
			return False
		else:
			played_cards = []
			for card_number in self.deck_cards:
				played_cards.append(card_number)
				self.deck_cards.remove(card for card in played_cards)
			for card in played_cards:
				print(card.__str__())

	def __str__(self):
		for card in self.deck_cards:
			print(card.__str__())