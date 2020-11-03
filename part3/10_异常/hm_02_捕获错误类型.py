#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_02_捕获错误类型.py
@time: 2020-10-28 11:19

"""
try:
    # 1. 提示用户输入一个整数
    num = int(input("请输入一个整数："))

    # 2. 使用`8`除以用户输入的整数并且输出
    result = 8 / num
    # if result == 0:
    print("输入的整数是 [%d]" % result)
except ZeroDivisionError:
    print("除0错误")
except ValueError:
    print("非数字错误")

