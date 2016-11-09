""" Module contains all necessary functions to generate complete
    minimization method Karnaugh
"""

from flip_flops import J, JK, K

tab = [0, 1, 3, 2, 4, 5, 7, 6, 12, 13, 15, 14, 8, 9, 11, 10]

file_header = r"""
\documentclass[11pt]{article}

\usepackage[margin=1in]{geometry}

\begin{document}
"""
file_footer = r'\end{document}'

hline = r'\hline'
end_tabular = r'\end{tabular}'


def gen_header():
    """ Function generates header for flip-flop table.

    :return: common table header
    """
    return 'Z' + subscript('Q', 2) + ' / ' + subscript('Q', 1) + subscript('Q', 0)


def to_bin(v, n=3):
    """ Function generates formatted int to bin.

    :param v: value to transform
    :param n: number of bits
    :return: formatted bin number
    """
    if v == '*':
        return '***'
    return '{0:0>{1}b}'.format(v, n)


def split(lst, n=4):
    """ Generator yields lst in parts.

    :param lst: list of elements
    :param n: length of each part
    """
    for i in range(len(lst) // n):
        yield lst[n * i:n * (i + 1)]


def complete_moves(moves):
    """ Function fills missing moves with '*'.

    :param moves: list of moves
    :return: completed, sorted list of moves
    """
    filled = list(moves)
    missing = set(range(8)) - set(i[-2] for i in filled)
    if len(moves[0]) == 3:
        for i in missing:
            filled.append((0, i, '*'))
            filled.append((1, i, '*'))
    else:
        for i in missing:
            filled.append((i, '*'))

    return sorted(filled)


def gen_Gray(n=2):
    """ Generator yields successive Gray numbers.

    :param n: number of bits
    """
    for i in range(1 << n):
        g = i ^ (i >> 1)
        yield '{0:0>{1}b}'.format(g, n)


def begin_tabular(n: int):
    """ Function returns opening tag for table.

    :param n: number of column in table
    :return: string which starts table
    """
    return r'\begin{tabular}{|' + 'c|' * n + '}'


def subscript(big, small):
    """ Function returns proper syntax for subscript.

    :param big: value which should be up and big
    :param small: value which should be down and small
    :return: string in Latex syntax
    """
    return '${}_{{{}}}$'.format(big, small)


def multicolumn(n: int, value=''):
    """ Function merges n columns and fills it with value.

    :param n: number of merged columns
    :param value: text in merged columns
    :return: string
    """
    return r'\multicolumn{{{}}}{{|c|}}{{{}}}'.format(n, value)


def gen_row(row):
    """ Function transforms list of items to one row from Latex.

    :param row: list of items
    :return: string, merged row
    """
    row = map(str, row)
    return ' & '.join(row) + r' \\'


def gen_tabular(rows, sep=' '):
    """ Function combines all parts of table.

    :param rows: list of rows
    :param sep: separator between rows
    :return: string, merged table
    """
    n = max(len(row) for row in rows)
    s = [begin_tabular(n)]

    for row in rows:
        s.append(gen_row(row))

    s.append(end_tabular)
    # sep = '\n'
    return '{0}{1}{0}'.format(sep, hline).join(s)


def gen_moves(moves):
    """ Function generates table of moves with 2 or 3 column

    :param moves: list of moves
    :return: string containing whole table
    """
    n = len(moves[0])
    rows = (
        [multicolumn(n, '')],
        ['t', 't+1'],
        *moves
    )

    if n == 3:
        rows[1].insert(0, 'Z')

    return gen_tabular(rows)


def gen_bin_moves(moves):
    """ Function generates table of moves in binary system with 2 or 3 column

    :param moves: list of moves
    :return: string containing whole table
    """
    n = len(moves[0])
    rows = (
        [multicolumn(3, 't'), multicolumn(3, 't+1')],
        [subscript('Q', i) for i in '210'] * 2,
        *[(*z, *to_bin(t), *to_bin(u)) for *z, t, u in moves]
    )

    if n == 3:
        rows[0].insert(0, '')
        rows[1].insert(0, 'Z')

    return gen_tabular(rows)


def gen_flip_flops(moves):
    """ Function generates table of JK flip-flops according to moves

    :param moves: list of moves
    :return: string containing whole table
    """
    rows = [
        [multicolumn(6, 'Przerzutniki')],
        [subscript(i, j) for j in '210' for i in 'JK']
    ]

    for *_, t, u in moves:
        it = zip(to_bin(t), to_bin(u))
        rows.append(sum([JK(*next(it)) for _ in '210'], ()))

    return gen_tabular(rows)


def gen_flip_flop_content(moves, ff, n):
    ff_map = {
        'J': J,
        'K': K,
    }

    l = tab[:]
    for i, (*_, t, u) in zip(l[:], moves):
        l[i] = ff_map[ff](to_bin(t)[2 - n], to_bin(u)[2 - n])
    return l


def gen_flip_flop(moves, ff, n):
    """ Function generates table ready to minimize

    :param moves: list of moves
    :param ff: type of flip-flop
    :param n: number of column
    :return: string containing whole table
    """

    content = gen_flip_flop_content(moves, ff, n)

    gg = gen_Gray()
    gl = split(content)
    rows = [
        [multicolumn(5, subscript(ff, n))],
        (gen_header(), *gen_Gray()),
        (next(gg), *next(gl)),
        (next(gg), *next(gl)),
    ]

    if len(moves[0]) == 3:
        rows.append((next(gg), *next(gl)))
        rows.append((next(gg), *next(gl)))

    return gen_tabular(rows)


if __name__ == '__main__':
    series = [int(i) for i in '0123654']
    moves = [(v, series[(i + 1) % len(series)]) for i, v in enumerate(series)]

    moves = [
        (0, 0, 1),
        (0, 1, 2),
        (0, 2, 3),
        (0, 3, 6),
        (0, 4, 0),
        (0, 5, 4),
        (0, 6, 5),

        (1, 0, 4),
        (1, 1, 0),
        (1, 2, 1),
        (1, 3, 2),
        (1, 4, 5),
        (1, 5, 6),
        (1, 6, 3),
    ]

    full_moves = complete_moves(moves)
    # print(moves)

    to_write = '\n'.join([
        file_header,
        '',
        gen_moves(moves),
        gen_bin_moves(moves),
        gen_flip_flops(moves),
        '',
        gen_flip_flop(full_moves, 'J', 2),
        gen_flip_flop(full_moves, 'K', 2),
        '',
        gen_flip_flop(full_moves, 'J', 1),
        gen_flip_flop(full_moves, 'K', 1),
        '',
        gen_flip_flop(full_moves, 'J', 0),
        gen_flip_flop(full_moves, 'K', 0),
        '',
        file_footer
    ])

    with open('file.tex', 'w') as f:
        f.write(to_write)

    print(gen_flip_flop_content(full_moves, 'J', 0))
