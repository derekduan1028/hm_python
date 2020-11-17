#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_05_函数的参数.py
@time: 2020-11-10 17:56

"""


# def sum_2_num():
#     """对两个数字的求和"""
#     num1 = 10
#     num2 = 20
#     result = num1 + num2
#     print("%d + %d = %d" % (num1, num2, result))
#
#
# sum_2_num()


def sum_2_num(num1, num2):
    """对两个数字的求和"""
    result = num1 + num2
    print("%d + %d = %d" % (num1, num2, result))


sum_2_num(10, 20)
