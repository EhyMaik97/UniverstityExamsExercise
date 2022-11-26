import logging
_logger = logging.getLogger("__name__")


class Album:
	"""identified by a progressive (natural) number, automatically initialized upon its creation,
	it will also contain an ordered list of tracks, the medium (choose between VINYL, CD, USB), a title and a performer
	(optional for your own mixes) and a capture date (possibly by reusing a library class)."""

	def __init__(self, code, tracks, support, title, performer, start_date):
		self.code = code
		self.support = support
		self.tracks = tracks
		self.title = title
		self.performer = performer
		self.start_date = start_date

	def add_tracks(self, tracks):
		if isinstance(tracks, list):
			self.tracks.extend(tracks)
		else:
			self.tracks.append(tracks)

	def check_existing_trace(self, trace):
		album_tracks_code = []
		for track in self.tracks:
			album_tracks_code.append(track.code)
		if trace.code in album_tracks_code:
			return True
		else:
			return False

	def get_duration_trace(self, trace):
		if self.check_existing_trace(trace):
			return trace.duration

	def get_total_duration(self):
		total_duration = 0.0
		for trace in self.tracks:
			total_duration += trace.duration
		return round(total_duration, 2)

	def cycle_by_duration(self):
		order_tracks = []
		for trace in sorted(self.tracks, key=lambda x: float(x.duration)):
			order_tracks.append(trace)
		return order_tracks

	def __str__(self):
		return "Album data with code: " + "'" + str(self.code) + "'\n" \
			"Title: " + self.title + ", Performer: " + self.performer + ", " \
			"Acquisition Date: " + self.start_date + ", Support: " + self.support + \
			", Total Duration: " + str(self.get_total_duration()) + " minutes"
