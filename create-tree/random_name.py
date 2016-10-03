""" Module contains class RandomName.
"""

from random import randrange, choice, sample

__all__ = 'RandomName',


class RandomName:
    """ Class generates random name.
    """
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxz'

    def __init__(self, syllables=None, spaces=None):
        self.syllables = syllables or randrange(1, 5)
        self.spaces = spaces or randrange(self.syllables)

        self.name = self.create_name()

    def create_name(self):
        """ Method creates random name specified by fields in the class.
        """
        name = [self.get_pair() for _ in range(self.syllables)]

        ind_spaces = sample(range(1, self.syllables), self.spaces)
        for i in sorted(ind_spaces, reverse=True):
            name.insert(i, ' ')

        return ''.join(name)

    def get_pair(self):
        """ Method returns random pair of consonant+vowel.
        """
        return choice(self.consonants) + choice(self.vowels)

    def get(self):
        """ Method returns name
        """
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'syl: {syllables}, spa: {spaces}, name: {name!r}'.format(**vars(self))


if __name__ == '__main__':
    for syl in range(10):
        for spa in range(syl):
            print(repr(RandomName(syl, spa)))
