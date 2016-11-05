from itertools import count

from graph import Graph


class BranchAndBound(Graph):
    def run(self):
        lb = self.reduce()
        print('lb', lb)
        print('min col', self.get_min_in_cols())
        print('min row', self.get_min_in_rows())
        print('min row2', self.get_min_in_rows_bb())
        print('min col2', self.get_min_in_cols_bb())
        return super().run()

    def reduce(self):
        lb = 0

        for ir, row_min, row in zip(count(), self.get_min_in_rows(), self):
            lb += row_min
            for ic, col in enumerate(row):
                if col == -1:
                    continue
                self[ir, ic] = col - row_min

        for ic, col_min, col in zip(count(), self.get_min_in_cols(), zip(*self)):
            lb += col_min
            for ir, row in enumerate(col):
                if row == -1:
                    continue
                self[ir, ic] = row - col_min

        return lb

    def get_min_in_rows_bb(self):
        l = []
        for ir, row in enumerate(self):
            if row.count(0) > 1:
                l.append(0)
                continue
            l.append(min(row, key=lambda x: self.ignore_value(x, 0)))

        return l

    def get_min_in_cols_bb(self):
        l = []
        for ic, col in enumerate(zip(*self)):
            if col.count(0) > 1:
                l.append(0)
                continue
            l.append(self.get_min_in_col(ic, 0))

        return l


if __name__ == '__main__':
    b = BranchAndBound.from_file('tsp/5.tsp')
    print(b)
    b = b.run()
    print(b)
