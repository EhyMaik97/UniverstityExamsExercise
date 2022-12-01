import random


class User:

    def __init__(self, name):
        self.id = ''.join(random.choice('0123456789ABCDEF') for i in range(5))
        self.name = name

    def __str__(self):
        return "User with id: " + str(self.id) + " - Name: " + self.name
