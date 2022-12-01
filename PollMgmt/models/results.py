import logging

from pip._internal.utils.misc import tabulate

_logger = logging.getLogger("__name__")


class Results:

    def __init__(self, users_n_answers, questions):
        data = [users_n_answers]
        self.table = tabulate(data)

    def compute_media(self):
        pass

    def compute_moda(self):
        pass

    def print_histogram(self):
        pass
