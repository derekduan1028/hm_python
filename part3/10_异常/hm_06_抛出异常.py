#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_06_抛出异常.py
@time: 2020-10-28 15:34

"""


def input_password():
    # . 提示用户输入密码
    pwd = input("请输入密码：")
    # . 判断密码长度，够8位返回用户输入的密码
    if len(pwd) >= 8:
        return pwd
    # . 不够8位，主动抛出异常
    print("主动抛出异常")
    # 创建异常对象
    ex = Exception("密码长度不够")
    # 主动抛出异常
    raise ex


# 提示用户输入密码
try:
    print(input_password())
except Exception as result:
    print(result)
