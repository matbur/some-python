f = '{:0>3b}'

hline = r'\hline'
end_tabular = r'\end{tabular}'


def begin_tabular(n):
    return r'\begin{tabular}{|' + 'c|' * n + '}'


def subscript(up, down):
    return '${}_{{{}}}$'.format(up, down)


def multicolumn(n, value):
    return r'\multicolumn{{{}}}{{|c|}}{{{}}}'.format(n, value)


def gen_row(row):
    row = map(str, row)
    return ' & '.join(row) + ' \\\\'


def gen_tabular(rows):
    n = len(rows[len(rows) // 2])
    s = [begin_tabular(n)]

    for row in rows:
        s.append(gen_row(row))

    s.append(end_tabular)
    sep = ' '
    # sep = '\n'
    return '{0}{1}{0}'.format(sep, hline).join(s)


def gen_moves(moves):
    rows = [('t', 't+1')]
    for t, u in moves:
        rows.append((t, u))
    return gen_tabular(rows)


def gen_bin_moves(moves):
    rows = [
        (multicolumn(3, 't'), multicolumn(3, 't+1')),
        [subscript('Q', i) for i in '210'] * 2
    ]
    for t, u in moves:
        t = f.format(t)
        u = f.format(u)
        rows.append((*t, *u))

    return gen_tabular(rows)


if __name__ == '__main__':
    moves = [(i, (i + 1) % 8) for i in range(8)]

    print(gen_moves(moves))
    print(gen_bin_moves(moves))
