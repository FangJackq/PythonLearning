#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-11-04 21:52:18
# @Author  : Thanks for Yong Lee Tell me how to build this Package (${email})
# @Link    : ${link}
# @Version : $Id$

import math
a=int(input('请输入你想要判断的素数'))
b=int(math.sqrt(a))
count=0
# print (b) 
for x in range (2,b):
    if a % x == 0 :
        count+=1
        print(x)
if count >= 2:
    print('%d是一个素数' %a)
else :
    print('%d不是一个素数' %a)
