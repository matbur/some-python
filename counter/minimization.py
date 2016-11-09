""" Module contains functions to minimize boolean function
    with method Quine-McCluskey.
"""

from flip_flops import J, K

fields = [0, 1, 3, 2, 4, 5, 7, 6, 12, 13, 15, 14, 8, 9, 11, 10]


def to_bin(value, width=3):
    """ Function generates formatted int to bin.

    :param value: value to transform
    :param width: number of bits
    :return: formatted bin number
    """
    if value == '*':
        return '***'
    return '{0:0>{1}b}'.format(value, width)


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


def gen_Gray(width=2):
    """ Generator yields successive Gray numbers.

    :param width: number of bits
    """
    for i in range(1 << width):
        g = i ^ (i >> 1)
        yield '{0:0>{1}b}'.format(g, width)


def gen_flip_flop_content(moves, f_f, num):
    """ Function generates interior table to minimize for flip-flop.

    :param moves: list of movements
    :param f_f: type of flip-flop
    :param num: number of column
    :return: list with table
    """
    ff_map = {
        'J': J,
        'K': K,
    }

    lst = fields[:]
    for i, (*_, t, u) in zip(lst[:], moves):
        t_n = to_bin(t)[2 - num]
        u_n = to_bin(u)[2 - num]
        lst[i] = ff_map[f_f](t_n, u_n)
    return lst


def group(minterms):
    """ Function groups items by number of 1s.

    :param minterms: list of items to group
    :return: grouped list of lists
    """
    if not minterms:
        return []

    first = minterms[0]
    size = len(first) - first.count('-') + 1
    grouped = [[] for _ in range(size)]
    for i in minterms:
        n = i.count('1')
        grouped[n].append(i)
    return grouped


def merge(this, other):
    """ Functions merges two minters to one similar.

    :param this: 1st minterm
    :param other: 2nd minterm
    :return: merged minterm
    """
    merged = []
    for i, j in zip(this, other):
        merged.append(i if i == j else '-')
    return ''.join(merged)


def like(this, other):
    """ Function checks if two given minterms differ in one position.

    :param this: 1st minterm
    :param other: 2nd minterm
    :return: bool
    """
    return sum(i != j for i, j in zip(this, other)) == 1


def get_signal(implicant, ind, signal):
    """

    :param implicant:
    :param ind: index of signal
    :param signal: names of signals
    :return: proper signal symbol
    """
    if implicant[ind] == '-':
        return ''
    if implicant[ind] == '0':
        return '/' + signal
    return signal


def get_minterm(implicant, signals):
    """

    :param implicant:
    :param signals: names of signals
    :return:
    """
    return ''.join(get_signal(implicant, i, v) for i, v in enumerate(signals))


def get_function(implicants, signals):
    """ Function generates whole boolean function.

    :param implicants: list of minimized implicants
    :param signals: names of signals
    :return: boolean function
    """
    return ' + '.join(get_minterm(i, signals) for i in implicants)


def get_unused(implicants, used):
    """ Function finds unused implicants from whole list.

    :param implicants: list of all implicants
    :param used: set of implicants which were used
    :return: set of unused implicants
    """
    set_implicants = set(sum((i for i in implicants), []))
    return set_implicants - used


def step(minterms):
    """ Function implements one step im minimization.

    :param minterms: list of minterms
    :return: tuple containing list of minterms and unused minterms
    """
    lst = []
    used = set()
    for i, j in zip(minterms, minterms[1:]):
        for x in i:
            for y in j:
                if not like(x, y):
                    continue

                lst.append(merge(x, y))
                used.add(x)
                used.add(y)
    return lst, get_unused(minterms, used)


def minimize(minterms, signals):
    """ Function generates boolean function from list of minterms.

    :param minterms: list of minterms
    :param signals: names of signals
    :return: boolean function
    """
    minterms = [to_bin(i, 4) for i in minterms]
    unused = set()
    for _ in range(5):
        minterms = group(minterms)
        minterms, s = step(minterms)
        unused |= s
    return get_function(unused, signals)


if __name__ == '__main__':
    # l = [0, 1, 2, 8, 10, 11, 14, 15]
    # l = [0, 1, 2, 4, 5, 6, 8, 9, 12, 13, 14]
    l = [4, 8, 10, 11, 12, 15] + [9, 14]
    print(minimize(l, 'abcd'))
    # print(minimize(l, ['Z', 'Q2', 'Q1', 'Q0']))
