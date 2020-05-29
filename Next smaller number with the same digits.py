#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/6 23:45
# @Author : ZhangYongjie
import numpy as np
import itertools
def next_smaller(n):
    if n < 10:
        return -1
    else:
        b = []
        c = []
        for i in str(n):
            b.append(i)
        s = list(itertools.permutations(b,len(b)))
        for i in range(len(s)):

            # print(s[i])
            number = ''.join(s[i])
            c.append(int(number))
            # print(number)
        c.sort()
        # print(c)
        # print((int(c[0]))==c[0])
        # for j in range(len(c) - 1):
        #
        #     if n > int(c[j]) and n == int(c[j + 1]):
        #         return int(c[j])
        # else:
        #     return -1
        # print(list(s[1]))

        index = c.index(n)
        if index-1 == -1 or c.count(c[0]) == len(s):
            return -1
        else:
            return c[index-1]
#time out


# next_smaller(132)
# print(next_smaller(102))
def res2():
    from itertools import permutations
    number=input()
    choices=list(map(int,number)) #split the number and convert it to integer list of digits
    res=permutations(number)      #produce all combinations of the digits
    res2=[]
    for i in res:
        res2.append(int(''.join(i)))
    res2=sorted(res2)
    a = res2[res2.index(int(number))+1]
    #time out

def res3(n):
    b = []
    for i in str(n):
        b.append(int(i))

    rev_b = b[::-1]
    print(rev_b)
    for a in range(1,len(rev_b)):
        if rev_b[a] > rev_b[a-1]:
            print(a)
            temp = rev_b[a-1]
            rev_b[a-1] = rev_b[a]
            rev_b[a] = temp

            print(rev_b)

            gg = rev_b[:a]
            print(gg)
            res = gg[::-1]+rev_b[a:]
            print(res)
            aa = res[::-1]
            print(aa)
            i = int("".join([str(i) for i in aa]))
            # print(i)
            return i
    return -1


def next_smaller_1(number):
    if number <=10:
        return -1
    else:
        new_number = number
        digit = list(str(number))  # there is no need to convert to numbers. Characters are ok.
        digits = len(digit)-1

        for index_1 in range(digits-1, -1, -1):  # this is prefered over while
            for index_2 in range(digits, index_1-1, -1):  # this is prefered over while
                if digit[index_2] < digit[index_1]:
                    digit[index_2], digit[index_1] = digit[index_1], digit[index_2]
                    _first = digit[0:index_1+1]
                    _second = digit[-1:index_1:-1]  # by just backward slicing, there's no need for sort
                    digit = _first + _second
                    new_number = int(''.join(digit))
                    return new_number
        return -1
def res4(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] > s[i+1]:
            print(i)
            t = s[i:]
            print(t)
            m = max(filter(lambda x: x<t[0], t))
            print(m)
            t.remove(m)
            t.sort(reverse=True)
            s[i:] = [m] + t
            print(s[i:])
            res = int("".join(s))
            if len(list(str(res))) != len(list(str(n))):
                return -1
            return res
    return -1
print(res4(732232223312))
"""
TRUE 
"""
