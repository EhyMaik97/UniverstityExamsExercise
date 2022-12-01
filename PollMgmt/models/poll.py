import logging
import random
from PollMgmt.models.user import User
from PollMgmt.models.question import Question
from PollMgmt.models.results import Results

_logger = logging.getLogger(__name__)


class Poll:

    users = []
    questions = []

    def __init__(self, questions_file, users_file):
        with open(questions_file, 'r') as quest:
            question_lines = quest.readlines()
            for line in question_lines:
                question_lines_split = line.split(',')
                question = Question(question_lines_split[0], question_lines_split[1], question_lines_split[2])
                _logger.warning(question)
            self.questions.append(question)
        with open(users_file, 'r') as usrs:
            users_lines = usrs.readlines()
            for user_line in users_lines:
                user = User(user_line)
            self.users.append(user)

    def get_results(self, users, questions):
        result = []
        for user in users:
            for question in questions:
                # if question.answer_type == 2:
                answer = question.vals_answer_closed.get(random.randint(1, 5))
                result.append(Results([user.id, answer], question))
        return result

    def __str__(self):
        # todo complete method
        return "Poll:"

    def write_file(self):
        with open("poll.txt", 'w') as output:
            output.write(self.__str__())
