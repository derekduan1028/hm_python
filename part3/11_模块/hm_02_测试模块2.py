#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_02_测试模块2.py
@time: 2020-10-28 17:16

"""


# 全局变量
title = "模块2"


# 函数
def say_hello():
    print("这是 %s" % title)


# 类
class Cat(object):
    pass


if __name__ == "__main__":
    say_hello()


