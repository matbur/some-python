from itertools import permutations

from graph import Graph


class BruteForce(Graph):
    def run(self):
        best = self.copy()

        for p in permutations(range(self._dim)):
            temp = self.copy()
            temp._path = p

            best = min(best, temp)

        self.assign(best)
        self.delete_edges()

        return self


if __name__ == '__main__':
    b = BruteForce.from_file('tsp/5.tsp')

    print(b)
    b.run()
    print(b)
