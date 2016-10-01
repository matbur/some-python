from glob import glob
import os

from episode import Episode


class Season(object):
    def __init__(self, dirname):
        self.dirname = dirname
        self.files = self.find_files()

    def find_files(self):
        return glob(os.path.join(self.dirname, '*.srt'))

    @property
    def episodes(self):
        for episode in self.files:
            yield Episode(episode)

    def __str__(self):
        return self.dirname

    def __repr__(self):
        return self.__str__()
