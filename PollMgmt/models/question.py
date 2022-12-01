import logging
_logger = logging.getLogger(__name__)


class Question:

    answer_type_dict = {1: 'Open', 2: 'Close'}
    vals_answer_closed = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}

    def __init__(self, id, question, answer_type):
        self.id = id
        self.question = question
        self.answer_type = self.answer_type_dict.get(answer_type)

    def __str__(self):
        return "Question with id: " + str(self.id) + " - Title: " + self.question + " - Type: " + str(self.answer_type)
