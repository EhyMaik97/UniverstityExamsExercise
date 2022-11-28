import logging
_logger = logging.getLogger("__name__")


class Vehicle:

    def __init__(self, license_plate, cost):
        self.license_plate = license_plate
        self.cost = cost

    def __str__(self):
        return "License Plate: " + str(self.license_plate) + " - Cost/unit: " + str(self.cost) + "$"


class Auto(Vehicle):

    def __init__(self, license_plate):
        super().__init__(license_plate, cost=10)


class Moto(Vehicle):

    def __init__(self, license_plate):
        super().__init__(license_plate, cost=25)