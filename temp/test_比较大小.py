#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: test_比较大小.py
@time: 11/18/20 1:43 PM

"""


def test_two_num(num1, num2):
    return num1 is num2


a = 5
b = 5
print(id(a))
print(id(b))

result = test_two_num(a, b)
print(result)


c = 10000
d = 10000
print(id(c))
print(id(d))
result2 = test_two_num(c, d)
print(result2)
