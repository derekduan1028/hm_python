#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_07_函数的嵌套调用.py
@time: 2020-11-11 09:18

"""

def test1():
    print("*" * 50)

def test2():
    print("-" * 50)
    test1()
    print("+" * 50)

test2()