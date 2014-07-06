#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
    Moduł drukuje rozszerzalny trójkąt Pascala.
'''


def factorial(n):
    '''
        Funkcja zwraca silnię z liczby n iteracyjnie.
        (int) -> (int)
    '''

    fac = 1
    if n > 1:
        for i in xrange(2, n + 1):
            fac *= i
    return fac


def binomial(n, k):
    '''
        Funkcja zwraca wartość symbolu Newtona n nad k,
        jeśli n jest niemniejsze niż k.
        (int, int) -> (int)
    '''

    f = factorial
    if n >= k:
        return f(n) / (f(k) * f(n - k))


def row(n, k=4):
    '''
        Funkcja zwraca n-ty wiersz trójkąta Pascala,
        w którym każda kolumna ma szerokość k (domyślnie 4).
        (int, [int]) -> (str)
    '''

    l = []
    for i in xrange(n + 1):
        l.append('{0:^{1}}'.format(binomial(n, i), k))
    return ''.join(l)


def triangle(n, k=1):
    '''
        Funkcja drukuje trójkąt Pascala o n+1 wierszach,
        w którym każdy ma szerokość najniższego.
        (int, [int]) -> ()
    '''

    x = len(str(binomial(n, n / 2))) + k
    y = len(str(row(n, x)))
    for i in xrange(n + 1):
        print '{0:^{1}}'.format(row(i, x), y)


if __name__ == '__main__':
    import sys

    try:
        INT1 = int(sys.argv[1])
    except IndexError:
        INT1 = 10
    except ValueError:
        print '{} is not a integer'.format(sys.argv[1])

    try:
        INT2 = int(sys.argv[2])
    except IndexError:
        INT2 = 1
    except ValueError:
        print '{} is not a integer'.format(sys.argv[2])

    try:
        triangle(INT1, INT2)
    except:
        pass
