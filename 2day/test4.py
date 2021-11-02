#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-11-02 21:28:02
# @Author  : Thanks for Yong Lee Tell me how to build this Package (${email})
# @Link    : ${link}
# @Version : $Id$
# 根据半径计算圆的面积
import cmath
pi = cmath.pi
print (pi)
r1 = float(input("请输入圆的半径:"))
r = float("%.2f" % r1)
print (r)
ares = pi * (r ** 2)
print ("圆的半径%.2f,圆的面积%.2f" %(r1,ares))
