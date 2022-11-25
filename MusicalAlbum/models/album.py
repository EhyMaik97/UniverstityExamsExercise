
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

	def add_trace(self, tracks):
		for trace in tracks:
			self.tracks.append(trace)

	def check_exsisting_trace(self, trace):
		if trace.code in self:
			return "This trace is on the album"
		else:
			return "This trace is not on the album"

	def get_duration_trace(self, trace):
		if trace.code in self:
			return trace.duration
		else:
			return "This trace is not on the album"

	def get_total_duration(self):
		for trace in self:
			return sum(trace.duration)

	def cycle_by_duration(self, tracks):
		# TODO To implement
		pass
		# return tracks.sort(key=trace.duration for trace in tracks)

	def __str__(self):
		# total_duration = self.get_total_duration()
		return "Album data with code: " + "'" + str(self.code) + "'\n" \
			"Title: " + self.title + ", Performer: " + self.performer + ", " \
			"Acquisition Date: " + self.start_date + "Support: " + self.support + ", " \
			 # ", Total Duration: " + str(total_duration)
