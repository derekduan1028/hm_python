#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_02_局部变量.py
@time: 11/17/20 5:12 PM

"""


def demo1():
    # 定义一个局部变量
    num = 10
    print("在demo1中定义的变量是 %d" % num)


def demo2():
    # print("%d" % num)
    pass

demo1()
demo2()
