#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/29 19:43
# @Author : ZhangYongjie
def solution(array_a, array_b):
    a = 0
    for i in range(len(array_a)):
        mu = (array_a[i]-array_b[i])**2
        a += mu
    return a/len(array_a)
    pass