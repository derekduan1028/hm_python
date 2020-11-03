#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_01_测试模块1.py
@time: 2020-10-28 17:14

"""

# 全局变量
title = "模块1"


# 函数
def say_hello():
    print("这是 %s" % title)


# 类
class Dog(object):
    pass


if __name__ == "__main__":
    say_hello()




