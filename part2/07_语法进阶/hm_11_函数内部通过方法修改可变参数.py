#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_11_函数内部通过方法修改可变参数.py
@time: 11/19/20 11:21 AM

"""


def demo(num_list):
    print("in function:")
    # 使用方法修改列表的内容
    num_list.append(9)
    print(num_list)
    print("function done")


gl_list = [1, 2, 3]
demo(gl_list)
print(gl_list)
