#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/29 19:45
# @Author : ZhangYongjie
import re

def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == '':
        return head+'1'
    return head +str(int(tail)+1).zfill(len(tail))