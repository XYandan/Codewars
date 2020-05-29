#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/20 20:18
# @Author : ZhangYongjie
import math

def encode(s, shift):
    p="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    flag_num = 0
    res = ''
    for i in s:
        if i.isalpha() or i ==" ":
            if i == " ":  # 判断为空格特殊情况
                res = res + i
                flag_num += 1
            else:
                a = p.find(i)  # 查找索引位置
                b = (a + shift + flag_num) % 26
                flag_num += 1
                if i.isupper():
                    res += p[b + 26]
                else:
                    res += p[b]
        else:
            res += i
    return res


def moving_shift(s,shift):
    res = encode(s,shift)
    cut = int(math.ceil(len(res) / 5.0))
    return [res[i: i + cut] for i in range(0, 5 * cut, cut)]



def demoving_shift(v,shift):
    p = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    flag_num = 0
    res = ''
    old = v[0]+v[1]+v[2]+v[3]+v[4]
    print(old)
    for i in old:
        if i.isalpha() or i == " ":
            if i == " ":  # 判断为空格特殊情况
                res = res + i
                flag_num += 1
            else:
                a = p.find(i)  # 查找索引位置
                b = (a - shift - flag_num) % 26
                flag_num += 1
                if i.isupper():
                    res += p[b + 26]
                else:
                    res += p[b]
        else:
            res += i
    return res



s =  "L'économie (du grec ancien) est une activité humaine qui consiste en la production, la distribution, ..."
v = moving_shift(s,1)
print(moving_shift(s,1))
a = demoving_shift(v,1)