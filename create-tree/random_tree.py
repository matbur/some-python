""" Module contains class RandomTree.
"""

from random import randrange

import yaml
from random_name import RandomName

__all__ = 'RandomTree',


# l = (str(i) for i in range(10 ** 10))
# RandomName = lambda: '{:0>2}'.format(next(l))


class RandomTree:
    """ Class generates random tree.
    """

    def __init__(self, height=None, width=None):
        self.height = height or randrange(1, 5)
        self.width = width or randrange(1, 5)

        self.tree = self.create_tree()

    def create_tree(self):
        """ Method creates whole tree.
        """
        root_name = str(RandomName())
        root = self.create_leaves()
        self.create_branch(0, root)
        return [{root_name: root}]

    def create_branch(self, level, branch):
        """ Method fills branch with leaves and other branches.
        """
        if level == self.height:
            return

        width = randrange(1, self.width + 1)
        for _ in range(width):
            name = str(RandomName())
            new_branch = self.create_leaves()
            self.create_branch(level + 1, new_branch)
            branch.append({name: new_branch})

    def create_leaves(self):
        """ Method returns list of random names.
        """
        width = randrange(1, self.width + 1)
        return [str(RandomName()) for _ in range(width)]

    def get(self):
        """ Method returns tree.
        """
        return self.tree

    def __str__(self):
        return str(self.tree)

    def __repr__(self):
        return 'hei: {height}, wid: {width}\n'.format(**vars(self)) + \
               yaml.dump(self.tree)


if __name__ == '__main__':
    print(
        repr(RandomTree(2, 2))
    )
