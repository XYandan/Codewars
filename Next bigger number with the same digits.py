#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/29 19:40
# @Author : ZhangYongjie
def swap_first_with_higher(digits):
    for pos in range(len(digits) - 1, 0, -1):
        if digits[0] < digits[pos]:
            digits[0], digits[pos] = digits[pos], digits[0]
            break
    return digits


def reversed_tail(digits):
    return [digits[0]] + digits[1:][::-1]


def next_bigger(num):
    digits = list(str(num))
    for pos in range(len(digits) - 1, 0, -1):
        if digits[pos-1] < digits[pos]:
            left = digits[:pos-1]
            right = reversed_tail(swap_first_with_higher(digits[pos-1:]))
            return int(''.join(left + right))

    return -1