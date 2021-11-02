#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-11-02 21:15:25
# @Author  : Thanks for Yong Lee Tell me how to build this Package (${email})
# @Link    : ${link}
# @Version : $Id$
# 将华氏温度转换为摄氏温度

import os
f = float(input('请输入华氏温度'))
c = (f - 32 ) / 1.8
print ("您输入的华氏温度是:", f)
print ("算出来的摄氏温度是：", c)
print ('%.2f华氏度 = %.2f摄氏度' %(f,c))
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')


