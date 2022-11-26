import logging

_logger = logging.getLogger("__name__")

value_dict = {1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'X', 11: 'J', 12: 'Q', 13: 'K'}
seed_dict = {1: 'C', 2: 'Q', 3: 'F', 4: 'P'}


class Card:
    """each characterized by a seed and a value using its own enumeration types."""

    def __init__(self, value, seed):
        self.value = value_dict.get(value)
        self.seed = seed_dict.get(seed)

    def __str__(self):
        return "" + str(self.seed) + "" + str(self.value)

    class Deck:
        """Linear structure of 52 distinct cards"""

        def __init__(self):
            deck_cards = []
            for seed in range(1, 5):
                for value in range(1, 14):
                    deck_cards.append(Card(value, seed))
            for card in deck_cards:
                print(card.__str__())

        def shuffle(self):
            pass
