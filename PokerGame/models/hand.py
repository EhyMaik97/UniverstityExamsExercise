import logging
_logger = logging.getLogger("__name__")


class Hand:
	"""Each trace has an automatic integer code, title and performer as strings,
	and its (non-negative) duration in seconds. A track is considered the same as another if it has the same code."""