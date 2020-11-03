#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_01_简单的异常捕获.py
@time: 2020-10-28 10:44

"""


# 提示用户输入一个整数
try:
    num = int(input("请输入一个整数: "))
except:
    # 错误处理代码
    print("请输入正确的整数")

print("-" * 50)

