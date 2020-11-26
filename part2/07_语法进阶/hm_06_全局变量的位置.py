#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_06_全局变量的位置.py
@time: 11/18/20 10:55 AM

"""
# 模块中所有的全局变量，需定义在所有函数的上方
a = 10


def demo():
    print("%d" % a)
    print("%d" % b)
    # print("%d" % c)


b = 20
demo()
c = 30
