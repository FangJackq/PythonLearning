#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-11-02 23:38:07
# @Author  : Thanks for Yong Lee Tell me how to build this Package (${email})
# @Link    : ${link}
# @Version : $Id$
year=int(input("请输入你想要查询的年份: "))

check= year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print("查询的年份是否为闰年:", check)
