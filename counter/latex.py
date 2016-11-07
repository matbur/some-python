class Latex:
    f = '{:0>3b}'

    hline = r'\hline'
    end_tabular = r'\end{tabular}'

    @staticmethod
    def begin_tabular(n):
        return r'\begin{tabular}{|' + 'c|' * n + '}'

    @staticmethod
    def subscript(up, down):
        return '${}_{{{}}}$'.format(up, down)

    @staticmethod
    def multicolumn(n, value):
        return r'\multicolumn{{{}}}{{|c|}}{{{}}}'.format(n, value)

    @staticmethod
    def gen_row(row):
        row = map(str, row)
        return ' & '.join(row) + ' \\\\'

    @staticmethod
    def gen_tabular(rows):
        n = len(rows[len(rows) // 2])
        s = [Latex.begin_tabular(n)]

        for row in rows:
            s.append(Latex.gen_row(row))

        s.append(Latex.end_tabular)
        sep = ' '
        # sep = '\n'
        return '{0}{1}{0}'.format(sep, Latex.hline).join(s)

    @staticmethod
    def gen_moves(moves):
        rows = [('t', 't+1')]
        for t, u in moves:
            rows.append((t, u))
        return Latex.gen_tabular(rows)

    @staticmethod
    def gen_bin_moves(moves):
        rows = [
            (Latex.multicolumn(3, 't'), Latex.multicolumn(3, 't+1')),
            [Latex.subscript('Q', i) for i in '210'] * 2
        ]
        for t, u in moves:
            t = Latex.f.format(t)
            u = Latex.f.format(u)
            rows.append((*t, *u))

        return Latex.gen_tabular(rows)


if __name__ == '__main__':
    l = Latex()
    moves = [(i, (i + 1) % 8) for i in range(8)]

    print(l.gen_moves(moves))
    print(l.gen_bin_moves(moves))
