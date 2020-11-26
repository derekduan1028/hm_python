#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_05_修改全局变量.py
@time: 11/18/20 10:47 AM

"""


num = 10
print(id(num))


def demo1():
    # 只是定义了一个同名的局部变量，不会修改到全局变量
    # global 关键字修饰的变量是一个全局变量
    # 在使用赋值语句时，就不会创建局部变量
    global num
    num = 99
    print("demo1 ==> %d" % num)
    print("demo1 ==> %d" % id(num))
    # 希望修改全局变量的值


def demo2():
    print("demo2 ==> %d" % num)


demo1()
demo2()