#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: 九九乘法.py
@time: 2020-11-09 14:43

"""
i = 1
while i <= 9:
    # print("i=%d" % i)
    j = 1
    while j <= i:
        # print("j=%d" % j)
        print("%d * %d = %d" % (j, i, i*j), end=" ")
        j += 1
    i += 1
    print("")
