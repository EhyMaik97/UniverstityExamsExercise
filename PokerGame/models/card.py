import logging

_logger = logging.getLogger("__name__")


class Card:
    """Each characterized by a seed and a value using its own enumeration types."""

    # 'A': Ace, 'J' Jack, 'Q' Queen, 'K' King
    value_dict = {1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K'}
    # '\U00002665': Hearts, '\U00002666' Diamonds, '\U00002663' Clubs, '\U00002660' Spades,
    seed_dict = {1: '\U00002665', 2: '\U00002666', 3: '\U00002663', 4: '\U00002660'}

    def __init__(self, value, seed):
        self.value = self.value_dict.get(value)
        self.seed = self.seed_dict.get(seed)

    def __str__(self):
        return "" + str(self.seed) + "" + str(self.value)