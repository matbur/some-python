class Letter(object):
    def __init__(self, letter):
        self.letter = letter

    def is_letter(self):
        return self.ascii in range(ord('a'), ord('z') + 1)

    @property
    def ascii(self):
        return ord(self.letter)

    def __eq__(self, other):
        return self.ascii == other.ascii

    def __gt__(self, other):
        return self.ascii > other.ascii

    def __ge__(self, other):
        return self == other or self > other

    def __hash__(self):
        return hash(self.letter)

    def __str__(self):
        return self.letter

    def __repr__(self):
        return self.__str__()
