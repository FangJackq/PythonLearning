#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-11-07 20:46:52
# @Author  : Thanks for Yong Lee Tell me how to build this Package (${email})
# @Link    : ${link}
# @Version : $Id$

"""
正整数的反转

Version: 0.1
Author: 骆昊
"""

num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)
