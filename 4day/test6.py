#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-11-04 22:02:44
# @Author  : Thanks for Yong Lee Tell me how to build this Package (${email})
# @Link    : ${link}
# @Version : $Id$

for i in range (0,10):
    for j in range (1,i+1):
        print('%d x %d = %d ' %(i,j,i*j),end='\t')
    print()