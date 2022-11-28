import logging

_logger = logging.getLogger(__name__)
from VehicleFleet.models.vehicle import Vehicle
from VehicleFleet.models.vehicle import Auto
from VehicleFleet.models.vehicle import Moto
from VehicleFleet.models.seat import Seat


class Park:

	seats_auto = Seat()
	seats_motor = Seat()

	def __init__(self, max_auto, max_moto):
		self.max_auto = max_auto
		self.max_moto = max_moto

	def enter_vehicle(self, vehicle):
		if vehicle is isinstance(Moto):
			self.seats_motor.take_seat(vehicle)
			self.seats_motor.__str__()
		elif vehicle is isinstance(Auto):
			self.seats_auto.take_seat(vehicle)
			self.seats_auto.__str__()

	def exit_vehicle(self, vehicle):
		if vehicle is isinstance(Moto):
			self.seats_motor.free_seat(vehicle)
			# todo stampa scontrino orario entrata e uscita, costo sosta
			raise NotImplemented()
		elif vehicle is isinstance(Auto):
			self.seats_auto.free_seat(vehicle)
			# todo stampa scontrino orario entrata e uscita, costo sosta
			raise NotImplemented()

	def tic(self, number_of_time):
		# TODO WTF?
		for _ in range(number_of_time):
			return number_of_time + 1

	def promo(self, code_plate):
		raise NotImplemented()
		# discount_percent = 10
		# lucky_plate = 'EF'
		# if code_plate.equals(lucky_plate):
		# 	return discount_percent
		# else:
		# 	print("Better Luck next time")
		# 	return False

	def get_state_seats(self):
		raise NotImplemented()

	# def __str__(self):
	# 	return ""