#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: calc_123.py
@time: 2020-11-06 09:35

"""

# 使用'1'、'2'、'3'拼成1个三位数，要求每个位上数字不能相同

lst = [1, 2, 3]
for i in lst:
    b = lst
    c = lst
    # print("i=%i" % i)
    for j in b:
        if i == j:
            continue
        # print("  j=%i" % j)
        for h in c:
            if i == h or j == h:
                continue
            print(i * 100 + j * 10 + h)
