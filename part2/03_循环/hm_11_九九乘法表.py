#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_11_九九乘法表.py
@time: 2020-11-10 11:07

"""

row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d = %d" %
              (col, row, col * row), end="\t")
        col += 1
    print("")
    row += 1
