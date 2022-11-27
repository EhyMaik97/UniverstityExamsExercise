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
            for num in range(card_number):
                played_cards.append(self.deck_cards[num])
                self.deck_cards.remove(self.deck_cards[num])

        return played_cards

    def number_cards_remaining(self):
        remaining_card = 0
        for remaining_card in range(len(self.deck_cards)):
            remaining_card += + 1
        return str(remaining_card)

    def __str__(self):
        for card in self.deck_cards:
            print(card.__str__())
