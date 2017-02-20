import copy
import random

from matplotlib import pyplot as plt


class Grid:
    def __init__(self, size, density):
        self.size = size
        self.density = density

        self.tab = None
        self.has_percolation = None
        self.steeped_points = None

        self.fill_tab()
        self.check_percolation()
        self.run_percolation()

    def fill_tab(self):
        density = self.density
        size = self.size
        area = size ** 2
        blocked_area = int(area * density)
        no_blocked_area = area - blocked_area
        array = [1 for _ in range(blocked_area)] + \
                [0 for _ in range(no_blocked_area)]
        random.shuffle(array)
        it = iter(array)
        self.tab = [[next(it) for _ in range(size)] for _ in range(size)]

    def check_percolation(self):
        tab = self.tab
        size = self.size
        get_neighbours = self.get_neighbours

        points = [(0, i) for i in range(size) if tab[0][i] == 0]
        # random.shuffle(points)

        for ind, (i, j) in enumerate(points):
            for n_i, n_j in get_neighbours(i, j):
                if (n_i, n_j) in points or tab[n_i][n_j]:
                    continue

                points.insert(ind + 1, (n_i, n_j))

                if n_i == size - 1:
                    self.has_percolation = True
                    index = points.index((n_i, n_j)) + 1
                    self.steeped_points = points[:index]
                    return

        self.has_percolation = False
        self.steeped_points = points

    def run_percolation(self):
        s = '*'
        tab = self.tab
        points = self.steeped_points
        for i, j in points:
            tab[i][j] = s

    def get_neighbours(self, x, y):
        size = self.size
        neighbours = (
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 0),
        )
        not_allowed = (-1, size)
        for i, j in neighbours:
            x_i = x + i
            y_j = y + j

            if x_i in not_allowed or y_j in not_allowed:
                continue

            yield (x_i, y_j)

    def show(self):
        tab = copy.deepcopy(self.tab)
        size = self.size

        black = (0, 0, 0)
        white = (1, 1, 1)
        orange = (1, .5, 0)

        color = {
            0: white,
            1: black,
            '*': orange
        }

        for i in range(size):
            for j in range(size):
                tab[i][j] = color[tab[i][j]]

        plt.imshow(tab, interpolation='nearest')
        plt.axis('off')
        plt.show()

    def __str__(self):
        return '\n'.join(''.join(map(str, i)) for i in self.tab) \
            .replace('1', '\u25ae').replace('0', ' ')

    def __repr__(self):
        return 'Grid({}, {:.2f}): {}'.format(self.size, self.density, self.has_percolation)


if __name__ == '__main__':
    grid = Grid(40, .3)
    # print(grid)
    print([grid])
    grid.show()
