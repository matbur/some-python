from line import Line


class Episode(object):
    def __init__(self, filename):
        self.filename = filename
        self.text = self.read_file()

    @property
    def lines(self):
        for raw_line in self.text.split('\n\n'):
            line = Line(raw_line)
            if line.is_created_properly():
                yield line

    def read_file(self):
        try:
            with open(self.filename) as fopen:
                return fopen.read()
        except FileNotFoundError:
            return ''

    def __str__(self):
        return self.filename

    def __repr__(self):
        return self.__str__()
