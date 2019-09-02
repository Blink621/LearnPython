# -*- coding: utf-8 -*-

#题目：利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法

def trim(s):
    a=len(s)
    b=c=0
    for i in range(a):
        if s[i]==' ':
            b=b+1
        else: 
            break
    for i in range(a):
        if s[-i]==' ':
            c=c+1
        else: 
            break
    s=s[b:a-c+1]
    return s

d=trim('  hello  world  ')
print(trim('  hello  world  '),len(d))
print(trim('   hello  world    '))
print(trim('    '))

#修改 
def trim(s):
    while len(s)>0 and s[:1]==' ':
        s=s[1:]
    while len(s)>0 and s[-1:]==' ':
        s=s[:-1]
    return s
