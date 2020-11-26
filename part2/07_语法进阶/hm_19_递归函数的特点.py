#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_19_递归函数的特点.py
@time: 11/20/20 10:53 AM

"""


def sum_number(num):
    print(num)
    # 递归的出口，但参数满足某个条件时，不再执行函数
    if num == 1:
        return
    # 自己调用自己
    sum_number(num - 1)


sum_number(3)




