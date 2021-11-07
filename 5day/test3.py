#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-11-07 21:00:18
# @Author  : Thanks for Yong Lee Tell me how to build this Package (${email})
# @Link    : ${link}
# @Version : $Id$

for x  in range (1,21):
    for y in range (1,34):
        z = 100 - x - y 
        if x * 5 + y * 3 + z / 3 == 100:
            print (x,y,z)