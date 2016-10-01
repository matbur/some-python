from letter import Letter


class Word(object):
    def __init__(self, word):
        self.word = word

    @property
    def letters(self):
        for sign in self.word:
            letter = Letter(sign)
            if letter.is_letter():
                yield letter

    def __eq__(self, other):
        if isinstance(other, Word):
            return self.word == other.word
        return self.word == other

    def __hash__(self):
        return hash(self.word)

    def __str__(self):
        return self.word

    def __repr__(self):
        return self.__str__()
