# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    delta=b**2-4*a*c
    if delta>0:
        s=math.sqrt(delta)
        x1=(-b+s)/(2*a)
        x2=(-b-s)/(2*a)
        return x1,x2
        print('方程有两个解，分别为%.2f和%.2f'%(x1,x2))
    elif delta<0:
        print('方程无实根')
    else:
        x=(-b)/(2*a)
        return x
        print('方程只有一个解，是%.2f'%x)

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
