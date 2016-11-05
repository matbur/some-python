from copy import deepcopy
from itertools import combinations


class PathError(Exception):
    pass


class Graph:
    width = 4

    def __init__(self, arg=None):
        if isinstance(arg, Graph):
            self.assign(arg)

        else:
            self._tab = arg or []
            self._dim = len(self._tab)
            self._path = list(range(self._dim))

    @classmethod
    def from_file(cls, filename):
        with open(filename) as f:
            file = f.readlines()

        return cls([[int(col) for col in row.split()] for row in file[1:]])

    def run(self):
        return self

    def copy(self):
        return deepcopy(self)

    def assign(self, other):
        self._tab = deepcopy(other._tab)
        self._dim = deepcopy(other._dim)
        self._path = deepcopy(other._path)

    def get_dim(self):
        return self._dim

    def get_range_dim(self):
        return range(self.get_dim())

    def get_tab(self):
        return [row[:] for row in self]

    def get_path(self):
        return list(self._path)

    def get_weight(self, row, col):
        return self[row][col]

    def set_weight(self, row, col, weight):
        self._tab[row][col] = weight

    def get_path_weight(self, path=None):
        path = path or self.get_path()
        tab = self.get_tab()

        if len(set(path)) != len(path):
            raise PathError('Bad permutation')

        s = tab[path[-1]][path[0]]
        for row, col in zip(path, path[1:]):
            weight = tab[row][col]
            if weight == -1:
                return None
            s += weight
        return s

    def get_row(self, row):
        return list(self._tab[row])

    def get_col(self, col):
        return list(zip(*self._tab))[col]

    def delete(self, key):
        row, col = key
        self._tab[row][col] = -1

    def get_min_in_row(self, row, ign=-1):
        return min(self.get_row(row), key=lambda x: self.ignore_value(x, ign))

    def get_min_in_col(self, col, ign=-1):
        return min(self.get_col(col), key=lambda x: self.ignore_value(x, ign))

    def get_min_in_rows(self, ign=-1):
        return [self.get_min_in_row(row, ign) for row in self.get_range_dim()]

    def get_min_in_cols(self, ign=-1):
        return [self.get_min_in_col(col, ign) for col in self.get_range_dim()]

    @staticmethod
    def ignore_value(value, ign=-1):
        return (value, 10 ** 10)[value in (-1, ign)]

    def get_edges(self, path=None):
        path = path or self.get_path()
        return {(i, j) for i, j in zip(path, path[1:])} | {(path[-1], path[0])}

    def get_all_edges(self):
        com = list(combinations(self.get_range_dim(), 2))
        return set(com + [i[::-1] for i in com])

    def get_linked_edges(self, edge):
        s = {edge, edge[::-1]}
        row, col = edge
        for i in self.get_range_dim():
            s.add((row, i))
            s.add((i, col))

        return s

    def delete_edges(self, path=None):
        all_edges = self.get_all_edges()
        if path:
            edges = path
        else:
            edges = all_edges - self.get_edges()

        for row, col in edges:
            del self[row, col]

    def __int__(self):
        return self.get_path_weight()

    def __lt__(self, other):
        return int(self) < int(other)

    def __eq__(self, other):
        return int(self) == int(other)

    def __gt__(self, other):
        return int(self) > int(other)

    def __getitem__(self, item):
        return self.get_row(item)

    def __setitem__(self, key, value):
        self.set_weight(*key, value)

    def __delitem__(self, key):
        self.delete(key)

    def __str__(self):
        dim = self.get_dim()

        fstr = '{{:>{}}}'.format(Graph.width) * (dim + 1)

        return (
            'dim: {}\n'.format(dim) +
            'path: <{}>\n'.format(str(self._path)[1:-1]) +
            'total weight: {}\n'.format(self.get_path_weight()) +
            'neighbours matrix:\n' +
            fstr.format(' ', *range(dim)) + '\n' +
            '\n'.join(fstr.format(i, *row) for i, row in enumerate(self))
        )


if __name__ == '__main__':
    g = Graph.from_file('tsp/3.tsp')

    print(g)

    g.delete_edges(g.get_linked_edges((1, 0)))
    print(g)
