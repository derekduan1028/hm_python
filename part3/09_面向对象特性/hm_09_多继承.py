#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_09_多继承.py
@time: 2020-10-22 22:02

"""


class A:
    def test(self):
        print("test method")


class B:
    def demo(self):
        print("demo method")


class C(A, B):
    """多继承可以让子类对象同时具有多个父类的属性和方法"""
    pass


# 创建C类对象
c = C()
c.test()
c.demo()
print(c.__doc__)

