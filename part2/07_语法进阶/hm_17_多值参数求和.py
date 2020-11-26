#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_17_多值参数求和.py
@time: 11/20/20 10:19 AM

"""


def sum_numbers(*args):
    num = 0
    for i in args:
        num += i
    return num


result = sum_numbers(1, 2, 3, 4, 5)
print("result : %d" % result)
