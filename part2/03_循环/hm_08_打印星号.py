#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_08_打印星号.py
@time: 2020-11-09 14:29

"""

# 在控制台连续输出5行`*`, 每一行星号的数量依次递增
# 由于用到行号，从数字1开始比较方便
row = 1
while row <= 5:
    print("*" * row)
    row += 1
