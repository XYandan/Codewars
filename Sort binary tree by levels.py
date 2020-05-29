#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/29 19:40
# @Author : ZhangYongjie
import operator
from functools import reduce

def tree_by_levels(root):
    res = []
    res1 = []
    if root == None:
        return res

    q = [root]
    while len(q) != 0:
        res.append([node.value for node in q])
        new_q = []
        for node in q:
            if node.left:
                new_q.append(node.left)
            if node.right:
                new_q.append(node.right)
        q = new_q
    return reduce(operator.add, res)