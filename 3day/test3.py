#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-11-03 21:51:23
# @Author  : Thanks for Yong Lee Tell me how to build this Package (${email})
# @Link    : ${link}
# @Version : $Id$

score = int(input('please enter your score :'))
grade = 'FLASE'
if score >= 100 or score < 0 :
    print ('please enter the right score')
elif score >= 90 :
    grade = 'A'
elif score >= 80 :
    grade = 'B'
elif score >= 70 :
    grade = 'C'
elif score >= 60 :
    grade = 'D'
else :
    grade = 'E'
print ('%d is %s' %(score,grade))

