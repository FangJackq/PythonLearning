#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-11-03 21:30:59
# @Author  : Thanks for Yong Lee Tell me how to build this Package (${email})
# @Link    : ${link}
# @Version : $Id$

name = input("please enter your name:")
password = input("please enter your password:")

if name == "admin" and password == "123456":
    print("the name password is clear")
else:
    print("the name password is wrong")