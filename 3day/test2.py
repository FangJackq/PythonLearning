#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-11-03 21:44:35
# @Author  : Thanks for Yong Lee Tell me how to build this Package (${email})
# @Link    : ${link}
# @Version : $Id$

vaule = float(input('请输入长度 :'))
unit = input('请输入单位 in or cm :')
if unit == 'in' :
    print('%.1f英寸 = %.1f厘米' %(vaule,vaule * 2.54))
elif unit == 'cm' :
    print('%.1f厘米 = %.1f英寸' %(vaule,vaule / 2.54))
else :
    print('请输入正确的单位')