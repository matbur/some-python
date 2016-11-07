""" In this module signals are:
        t = Q(t)
        u = Q(t+1)
"""

def J(t, u):
    """ JK flip-flop
        t|u|J
        0|0|0
        0|1|1
        1|0|2
        1|1|2
    """
    return (u, 2)[t]


def K(t, u):
    """ JK flip-flop
        t|u|K
        0|0|2
        0|1|2
        1|0|1
        1|1|0
    """
    return (2, 1 - u)[t]


def D(t):
    """ D flip-flop
        t|D
        0|0
        1|1
    """
    return t


def T(t, u):
    """ T flip-flop
        t|u|T
        0|0|0
        0|1|1
        1|0|1
        1|1|0
    """
    return int(t != u)


if __name__ == '__main__':
    print('t u J K D T')
    for i in range(2):
        for j in range(2):
            print(i, j, J(i, j), K(i, j), D(j), T(i, j))
