from random import sample, shuffle, choice


class Base(object):
    def __init__(self, questions=None):
        self.questions = questions or []
        self.sample = sample(self.questions, min(len(self.questions), 20))

    def shuffle_questions(self):
        shuffle(self.questions)

    def get_random_question(self):
        return choice(self.questions)

    def __repr__(self):
        return '\n\n'.join(map(str, self.questions))
