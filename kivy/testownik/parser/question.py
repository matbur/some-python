from random import shuffle

from tools import is_image, get_number, get_img_path


class Question(object):
    def __init__(self, nr, text, answers, base):
        self.nr = get_number(nr)
        self.value = 3
        self.text = text
        self.is_img = is_image(text, base)
        self.img_path = get_img_path(self.is_img, self.text, base)
        self.answers = answers or []

    def shuffle_answers(self):
        shuffle(self.answers)

    def __repr__(self):
        return '{nr}){is_img} {text}\n\t{}'.format('\n\t'.join(map(str, self.answers)),
                                                   **self.__dict__)
