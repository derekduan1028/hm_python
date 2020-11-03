#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_05_异常的传递.py
@time: 2020-10-28 15:00

"""


def demo1():
    return int(input("请输入一个整数："))


def demo2():
    return demo1()


try:
    demo2()
except ValueError:
    print("不是一个整数")
except Exception as result:
    print("未知错误 [%s]" % result)
else:
    pass
finally:
    print("-" * 50)

