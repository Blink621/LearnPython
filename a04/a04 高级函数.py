# -*- coding: utf-8 -*-

from functools import reduce

def f(s):
    s[:1].upper
    s[1:].lower
    return s

def normalize(name):
    r=map(f,name)
    print(list(r))

L1 = ['adam', 'LISA', 'barT']
normalize(L1)

def g(x,y):
    return x*y

def prod(L):
    return reduce(g,L)
    
print(prod([3, 5, 7, 9]))

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9.}

def str2float(str):
    def fn(x, y):
        return x * 10 + y
    n=str.index('.')
    def char2num(str):
        return DIGITS[str]
    s1 = list(map(int,(x for x in str[: n])))
    s2 = list(map(int,(x for x in str[n + 1 :])))
    return reduce(fn,s1) + reduce(fn,s2)/10 ** len(s2)

print(str2float('123.456'))
