#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_16_多值参数.py
@time: 11/20/20 9:00 AM

"""


def demo(num, *args, **kwargs):
    # print(num)
    # print(args)
    # print(kwargs)
    return num, args, kwargs


a,b,c = demo(1, 2, 3, name="xiaoming", age=18)
print(a)
print(b)
name, age = c.values()
print("name:%s" % name)
print("age:%d" % age)



