#!/usr/bin/python
from pprint import pprint

fname = 'rpn2.py'

l = []
with open(fname) as f:
    b = False
    for i in f:
        i = i.strip(' \n')

        if 'end_' in i:
            b = not b

        if b and i and i[0] != '#':
            print(i)
            l.append(i)

        if 'begin' in i:
            b = not b



print sum(map(len, l))
