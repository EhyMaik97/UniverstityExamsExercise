import time
import logging
import random
from PokerGame.models.match import Match

_logger = logging.getLogger(__name__)


class Test:

	def main(self):
		match = Match()
		match.__str__()
		time.sleep(2)

		change_card_probability_player_1 = random.randint(0, 1)
		if change_card_probability_player_1 == 1:
			print("...Changing cards for player 1")
			time.sleep(2)
			match.ask_change_cards(match.player1, [1, 3])

		change_card_probability_player_2 = random.randint(0, 1)
		if change_card_probability_player_2 == 1:
			print("...Changing cards for player 2")
			time.sleep(2)
			match.ask_change_cards(match.player2, [0, 2, 4])

		change_card_probability_player_3 = random.randint(0, 1)
		if change_card_probability_player_3 == 1:
			print("...Changing cards for player 3")
			time.sleep(2)
			match.ask_change_cards(match.player3, [0, 1])

		change_card_probability_player_4 = random.randint(0, 1)
		if change_card_probability_player_4 == 1:
			print("...Changing cards for player 4")
			time.sleep(2)
			match.ask_change_cards(match.player4, [2, 4])

		change_card_probability_player_5 = random.randint(0, 1)
		if change_card_probability_player_5 == 1:
			print("...Changing cards for player 5")
			time.sleep(2)
			match.ask_change_cards(match.player5, [1, 2, 3, 4])

		print("Number of cards remaining in deck: " + str(match.deck.number_cards_remaining()))
		time.sleep(2)
		print("After players have dealt cards, here are the updated results: ")
		match.__str__()