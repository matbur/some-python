import re

from word import Word


class Line(object):
    pattern = re.compile(r"""(
            (?P<index>\d+)
            \n
            (?P<begin>\d+:\d+:\d+,\d+)
            \W+
            (?P<end>\d+:\d+:\d+,\d+)
            \n
            (?P<text>.*)
            )?""", re.VERBOSE | re.DOTALL)

    def __init__(self, raw_line):
        self.line = raw_line
        line = self.parse_line().groupdict()
        self.index = line['index']
        self.begin = line['begin']
        self.end = line['end']
        self.text = line['text']

        self.sub_n_prim_t()
        self.sub_prim_m()
        self.sub_prim_s()
        self.sub_prim_re()
        self.sub_prim_ll()

    def is_created_properly(self):
        return all(self.__dict__.values())

    @property
    def words(self):
        text = re.sub('\W', ' ', self.text).lower()
        for word in text.split():
            yield Word(word)

    def sub_n_prim_t(self):
        self.text = re.sub("n't", ' not', self.text or '')

    def sub_prim_m(self):
        self.text = re.sub("'m", ' am', self.text)

    def sub_prim_s(self):
        self.text = re.sub("'s", ' is', self.text)

    def sub_prim_re(self):
        self.text = re.sub("'re", ' are', self.text)

    def sub_prim_ll(self):
        self.text = re.sub("'ll", ' will', self.text)

    def parse_line(self):
        return self.pattern.match(self.line)

    def __str__(self):
        return '{index} {text!r}'.format(**self.__dict__)

    def __repr__(self):
        return self.__str__()
