#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_20_递归求和.py
@time: 11/20/20 11:06 AM

"""


# 1. 定义一个函数 sum_numbers
def sum_number(num):
    # 出口
    if num == 1:
        return 1
    # 2. 数字的累加 num + (1...num-1)
    # 假设sum_numbers 能够正确处理 1...num-1
    temp = sum_number(num - 1)
    return temp + num


result = sum_number(3)
print("result: %d" % result)






sum_number(3)