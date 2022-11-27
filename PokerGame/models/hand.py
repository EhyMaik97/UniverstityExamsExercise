import logging

_logger = logging.getLogger("__name__")


class Hand:
    """Consisting of 5 cards"""

    def __init__(self, cards):
        self.cards = cards

    def compute_score(self):
        points = 0
        cards_value = []
        cards_seed = []
        for card in self.cards:
            """I save the values (and seeds) of the cards of the hand in a list, going to retrieve them from the dictionary in the card class"""
            cards_value.append(list(card.value_dict.keys())[list(card.value_dict.values()).index(card.value)])
            cards_seed.append(list(card.seed_dict.keys())[list(card.seed_dict.values()).index(card.seed)])

        cards_value.sort()
        cards_seed.sort()
        value_elements_repeated = {i: cards_value.count(i) for i in cards_value}
        seed_elements_repeated = {i: cards_seed.count(i) for i in cards_seed}
        # Max seed needs for Flush: if max_seed == 5
        max_seed = max(seed_elements_repeated.values())
        max_value = max(value_elements_repeated.values())
        # Number of Max value needs for Double Pair: if max_value == 2 and number_of_max == 2
        number_of_max = [key for key, value in value_elements_repeated.items() if value == max(value_elements_repeated.values())]
        # No Point
        if max_value == 1 and not max_seed == 5:
            return "Nothing: " + str(points)
        # Pair
        if max_value == 2 and len(number_of_max) != 2 and not max_seed == 5:
            points += 1
            return "Pair - Score: " + str(points)
        # Double Pair
        elif max_value == 2 and len(number_of_max) == 2 and not max_seed == 5:
            points += 2
            return "Double Pair - Score: " + str(points)
        # Tris
        elif max_value == 3 and not max_seed == 5:
            points += 3
            return "Tris - Score: " + str(points)
        # Straight
        # elif
        #     points += 4
        #     return "Straight - Score: " + str(points)
        # Flush
        elif max_seed == 5:
            points += 5
            return "Flush - Score: " + str(points)
        # Full
        elif max_value == 3 and len(number_of_max) == 1:
            points += 6
            return "Full - Score: " + str(points)
        # Poker
        elif len(number_of_max) == 4:
            points += 7
            return "Poker - Score: " + str(points)
        # Royal Straight
        # elif
        #     points += 8
        #     return "Royal Straight - Score: " + str(points)

    def replace_cards(self, old_cards, new_cards):
        """In input I will give the position of the cards I want to change -> ♥2, ♣8, ♦10, ♥3, ♣10 -> I want to change: ♣8 and ♥3, I will input their position in the hand, i.e. [1,3] """
        if len(old_cards) < 1 or len(old_cards) > 5:
            print("Enter a valid number: 1 <= n <= 5 ")
            return False
        else:
            old_cards_to_remove = sorted(old_cards, reverse=True)
            for index in old_cards_to_remove:
                if index < len(self.cards):
                    self.cards.pop(index)
            for new_cards_to_add in new_cards:
                self.cards.append(new_cards_to_add)

        return self.cards

    def __str__(self):
        for card in self.cards:
            print(card.__str__())
