#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_10_不可变和可变参数.py
@time: 11/19/20 11:11 AM

"""


def demo(num, num_list):
    print("in function")
    # 函数内部的赋值语句给参数赋值
    num = 99
    num_list = [1, 2, 3]

    print(num)
    print(num_list)
    print("function done")


gl_num = 100
gl_list = [4, 5, 6]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)
