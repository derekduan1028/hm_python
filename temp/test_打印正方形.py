#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: test_打印正方形.py
@time: 11/18/20 4:45 PM

"""


def print_lines(str1, str2, wide):
    print(str1, end=" ")
    for i in range(wide):
        print(str2, end=" ")
    print(str1, end=" ")
    for i in range(wide):
        print(str2, end=" ")
    print(str1, end=" ")


a = 10
for j in range(0, 11):
    if j % 5 == 0:
        print_lines("+", "-", a)
        print("\t")
    else:
        print_lines("|", " ", a)
        print("\t")

