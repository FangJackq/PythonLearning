#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-11-03 21:59:03
# @Author  : Thanks for Yong Lee Tell me how to build this Package (${email})
# @Link    : ${link}
# @Version : $Id$

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积: %f' % (area))
else:
    print('不能构成三角形')