""" Module contains class RandomName.
"""

from random import randrange, choice, sample

__all__ = 'RandomName',


class RandomName(object):
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
        name = []
        for _ in range(self.syllables):
            name.append(self.get_pair())

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

    def debug(self):
        """ Method returns all information about the instance.
        """
        return 'syl: {syllables}, spa: {spaces}, name: {name!r}'.format(**vars(self))

    def __str__(self):
        return self.name

    def __repr__(self):
        return repr(self.name)


if __name__ == '__main__':
    for syl in range(10):
        for spa in range(syl):
            print(RandomName(syl, spa).debug())
