#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-11-07 21:25:18
# @Author  : Thanks for Yong Lee Tell me how to build this Package (${email})
# @Link    : ${link}
# @Version : $Id$
# practice the Fibonacci sequence

a = 0 
b = 1
c = 0
while c < 1000 :
    c = a + b 
    print (c,end='  ')
    a = b 
    b = c 


