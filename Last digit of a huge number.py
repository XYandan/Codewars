#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/29 19:42
# @Author : ZhangYongjie
def last_digit(lst):
    # Your Code Here
    n = 1
    for x in reversed(lst):
        n = x ** (n if n < 4 else n % 4 + 4)
    return n % 10

    pass