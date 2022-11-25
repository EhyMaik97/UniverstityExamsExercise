
class Trace:
	"""Each trace has an automatic integer code, title and performer as strings,
	and its (nonnegative) duration in seconds. A track is considered the same as another if it has the same code."""

	def check_traccia(self, tracks):
		for trace in tracks:
			pass
			# TODO Check that if there are duplicates for auto_code then they are duplicates

	def __init__(self, code, title, performer, duration):
		self.code = code
		self.title = title
		self.performer = performer
		self.duration = duration if duration > 0.0 else "You cannot create a track with duration less than or equal to 0"

	def __str__(self):
		return "Track data with code: " + "'" + str(self.code) + "'\n" \
			"Title: " + self.title + ", Performer: " + self.performer + ", Duration: " + str(self.duration)