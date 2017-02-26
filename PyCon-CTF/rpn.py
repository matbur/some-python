#!/usr/bin/python

from time import sleep

'begin'
def result(e):
    s=[]
    p=s.pop
    [s.append(float(v)
              if
              v
              not
              in
              '-+*/^'
              else
              eval('(%s)%s%s'%(p(-2),v.replace('^','**'),p())))
     for
     v
     in
     e.split()]
    return round(p(),2)
'end_'

from operator import *

def result2(e):
    s=[]
    for v in e.split():
        if v in '-+*/^':
            s[-2:]=[eval('(%s)%s%s'%(s[-2],v.replace('^','**'),s[-1]))]
        else:
            s+=[float(v)]
    return round(s[-1],2)

def result3(e):
    reduce(lambda x,y:eval('(%s)%s%s'%(x,v.replace('^','**'),y)))


def result2(e):
    s= []
    p=s.pop
    [s.append(float(v)
              if
              v
              not
              in
              '-+*/^'
              else
              eval('({2}){0}{1}'.format(v.replace('^',
                                                  '**'),p(),p())))
     for
     v
     in
     e.split()]
    return round(p(),2)



def ass(e, a):
    assert result(e) == a, '{} = {}'.format(e, a)

ass('3 5 + 7 2 - *', 40)
ass('5 1 2 + 4 * + 3 - ', 14)
ass('4 2 5 * + 1 3 2 * + /', 2)
ass('3 2 ^', 9)
ass('2.5 2 ^', 6.25)
ass('-2.5 2 ^', 6.25)
ass('2 -2 ^', 0.25)
ass('4.4 5 ^', 1649.16)
ass('1 2 + 4 * 3 +', 15)
ass('1 4 + 3 7 + * 5 /', 10)
ass('9 5 3 + 2 4 ^ - +', 1)
ass(' 162 2 1 + 4 ^ / ', 2)
ass(' 6 3 2 ^ - 11 - ', -14)
ass(' 6 3 - 2 ^ 11 - ', -2)
ass('1 2 3 + +', 6)
