import logging

_logger = logging.getLogger("__name__")


class Seat:

    dict_state = {0: 'FREE', 1: 'OCCUPIED'}

    def __init__(self):
        self.vehicle = None # TODO I need that?
        self.state = self.dict_state.get(0)

    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.state = self.dict_state.get(1)

    def take_seat(self, vehicle):
        self.state = self.dict_state.get(1)
        self.vehicle = vehicle

    def free_seat(self, vehicle):
        self.state = self.dict_state.get(0)
        self.vehicle = vehicle

    def __str__(self):
        if self.state == self.dict_state.get(1):
            return "Seat occupied by" + str(self.vehicle.license_plate)
        else:
            return "Seat free"
