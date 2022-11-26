import random
import datetime
import logging
_logger = logging.getLogger(__name__)

from PokerGame.models.card import Card
from PokerGame.models.deck import Deck
from PokerGame.models.hand import Hand


class Test:

	def main(self):
		deck = Deck()
		deck.shuffle()
		# deck.__str__()
		deck.give_cards(2)




