""" Module provides functions which emulate flip-flops
    commonly used in electronics circuits.

    In this module signals are:
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
    if '*' in (t, u):
        return '*'
    t = int(t)
    u = int(u)
    return (u, '*')[t]


def K(t, u):
    """ JK flip-flop
        t|u|K
        0|0|2
        0|1|2
        1|0|1
        1|1|0
    """
    if '*' in (t, u):
        return '*'
    t = int(t)
    u = int(u)
    return ('*', 1 - u)[t]


def JK(t, u):
    """ Returns combined result of J and K as tuple.
    """
    return J(t, u), K(t, u)


def D(t):
    """ D flip-flop
        t|D
        0|0
        1|1
    """
    if t == '*':
        return '*'
    return int(t)


def T(t, u):
    """ T flip-flop
        t|u|T
        0|0|0
        0|1|1
        1|0|1
        1|1|0
    """
    if '*' in (t, u):
        return '*'
    return int(t != u)


if __name__ == '__main__':
    print('t u J K D T')
    for i in range(2):
        for j in range(2):
            print(i, j, J(i, j), K(i, j), D(j), T(i, j), JK(i, j))
