#!/usr/bin/python3



def result(a):
    a=sum(a,[])
    for x,y,z in [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]:
        b=a[x]
        if b==a[y]==a[z]:
            return b
    return 'D'



assert result([['.', 'O', 'X'], ['X', 'X', 'X'], ['O', 'O', '.']]) == 'X'

assert result([['X', 'O', 'O'], ['X', 'O', 'X'], ['O', '.', '.']]) == 'O'

assert result([['X', 'O', 'X'], ['X', 'O', 'X'], ['O', '.', '.']]) == 'D'
