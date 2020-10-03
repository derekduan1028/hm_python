#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: lesson1.py
@time: 2020-09-01 09:59

"""

print("hello python3!")


def get_num(n):
    for i in range(n):
        print(i)
        return i


a = get_num(8)
print(a)
