import random
from models.album import Album
from models.trace import Trace
import datetime


class Test:

	def take_random_date(self):
		start_date = datetime.date(2020, 1, 1)
		end_date = datetime.date(2020, 2, 1)
		time_between_dates = end_date - start_date
		days_between_dates = time_between_dates.days
		random_number_of_days = random.randrange(days_between_dates)
		return start_date + datetime.timedelta(days=random_number_of_days)

	def main(self):
		track_title = ["AUDIO", "DASERT", "EAGLE", "Ak!", "kINEPE", "TEASE", "SmoNEY", "OSAAE", "Cashe3", "BandicOTtt", "Crash"]
		album_title = ["MyloXiloto", "AlbumBellissimo", "RockAlbum", "All best jazz", "Rap n Rock", "CashNoMoney", "Cyber"]
		support = ["VINILE", "CD", "USB"]
		track_performer = ["MIKE", "GIOVANNI", "MICHELE", "DAVIDE", "CORRADO", "CRISTIANO", "HERNANDEZ", "CIRO", "LUIS", "FEDEZ"]
		track_duration = [1.2, 4.5, 2.3, 5.0, 1.23, 4.53, 5.22, 4.12, 3.35, 5.21, 6.01, 2.35, 6.23, 2.43, 3.12, 3.13]
		tracks = []
		album = []
		for number in range(100):
			tracks.append(Trace(number, random.choice(track_title), random.choice(track_performer), random.choice(track_duration)))

		five_tracks = random.sample(tracks, 5)
		for number in range(12):
			album.append(Album(number, five_tracks, random.choice(support), random.choice(album_title), random.choice(track_performer), str(self.take_random_date())))

		for alb in album:
			print(alb.__str__())
		
		for tracks in album[0].tracks:
			print(tracks.__str__())


