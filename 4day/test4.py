#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-11-04 21:39:13
# @Author  : Thanks for Yong Lee Tell me how to build this Package (${email})
# @Link    : ${link}
# @Version : $Id$

import random
number = random.randint(0,100)
count = 0
while True:
    guess=int(input('please guess a number between 0 and 100:'))
    count += 1
    if guess > number:
        print('too high')
    elif guess < number:
        print('too small')
    else :
        break
if count <= 7 :
    print('great the number is %d ,you use %d time to guess it' %(number,count))
else:
    print ('your IQ is low the number is %d ,you use %d time to guess it' %(number,count))
