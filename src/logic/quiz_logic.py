from utils.file_handler import getQuestion
import random, base64


def decode_base64(data):
    return base64.standard_b64decode(data).decode(encoding="utf-8", errors="replace")

class QuizLogic(object):
    
    def __init__(self):
        self.questions = []
        self.answers = []
        self.options = []

    def organize(self, questions):
        for question in questions:
            self.questions.append(decode_base64(question['question']))
            options: list = [decode_base64(option) for option in question['incorrect_answers'] + [question['correct_answer']]]
            random.shuffle(options)
            self.options.append(options)
            self.answers.append(options.index(decode_base64(question['correct_answer'])))
    
    def get_answers(self):
        return self.answers

    def get_question(self):
        for question_no, question, option in zip(range(1, 51), self.questions, self.options):
            yield (question_no, question, option)
        yield -1, "End", "End"
        
    
    def calculate_score(self, marked_answer):
        return sum([answer == marked for answer, marked in zip(self.answers, marked_answer)])

    def fetch_questions(self, url):
        questions = getQuestion(url)
        self.organize(questions)