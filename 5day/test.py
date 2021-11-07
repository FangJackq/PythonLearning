#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-11-07 20:41:58
# @Author  : Thanks for Yong Lee Tell me how to build this Package (${email})
# @Link    : ${link}
# @Version : $Id$

for x in range (100,1000):
    a = x // 100
    b = x // 10 % 10 
    c = x %  10
    if a ** 3 + b ** 3 + c ** 3 == x :
        print (x)

