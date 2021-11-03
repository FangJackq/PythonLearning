#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-11-03 21:36:47
# @Author  : Thanks for Yong Lee Tell me how to build this Package (${email})
# @Link    : ${link}
# @Version : $Id$

x = float(input("请输入X的值: "))
if x > 1 :
    y = 3 * x - 5
elif x >= -1  and x <= 1:
    y = x + 2
else:
    y = 5 * x + 3
print("函数的结果是：%.2f" %y)