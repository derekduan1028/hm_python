#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_12_面试题加等于.py
@time: 11/19/20 11:35 AM

"""


def demo(num, num_list):
    print("in function")
    # num = num + num
    num += num

    # num_list += 等于调用列表的expend方法
    num_list += num_list
    print(num)
    print(num_list)
    print("function done")


gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)

