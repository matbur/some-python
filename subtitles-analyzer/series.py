from glob import glob
import os

from season import Season


class Series(object):
    def __init__(self, dirname):
        self.dirname = dirname
        self.dirs = self.find_dirs()

    def find_dirs(self):
        return glob(os.path.join(self.dirname, '*'))

    @property
    def seasons(self):
        for season in self.dirs:
            yield Season(season)
