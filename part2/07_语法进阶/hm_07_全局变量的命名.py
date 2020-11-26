#!/usr/bin/python
# coding:utf-8


"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_07_全局变量的命名.py
@time: 11/19/20 9:34 AM

"""

gl_num = 10

gl_title = "hm programmer"

gl_name = "xiaoming"


def demo():
    num = 99
    print("%d" % num)
    print("%s" % gl_title)
    print("%s" % gl_name)


demo()

