# -*- coding: utf-8 -*-

#题目：请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(L):
    b=len(L)
    max=min=L[0]
    for a in range(b):
        if L[a]>max:
            max=L[a]
        if L[a]<min:
            min=L[a]
    s=(min,max)
    return s

print(findMinAndMax([7, 1, 3, 9, 5]))
