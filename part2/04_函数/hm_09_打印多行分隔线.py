#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_09_打印多行分隔线.py
@time: 2020-11-11 09:59

"""


def print_line(chr, times):
    """
    打印多行分隔线
    :param chr: 分隔线使用的分隔字符
    :param times: 分隔线重复的次数
    """
    print(chr * times)


def print_lines(char, times):
    row = 0
    while row < 5:
        print_line(char, times)
        row += 1


print_lines("+", 50)

