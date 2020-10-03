#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: test_repeat_function.py
@time: 2020-09-16 15:31

"""


def repeat_print():
    print("this is repeat:")
    print_hello()
    print_hello()


def print_hello():
    print("hello world!")


repeat_print()
