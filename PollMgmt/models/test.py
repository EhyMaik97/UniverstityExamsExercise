import time
import logging
import random
from PollMgmt.models.poll import Poll
from PollMgmt.models.results import Results
from PollMgmt.models.question import Question

_logger = logging.getLogger(__name__)


class Test:

	def main(self):
		poll = Poll('questions.txt', 'users.txt')
		_logger.warning("Poll")
		results = poll.get_results(poll.users, poll.questions)
		print(results)
