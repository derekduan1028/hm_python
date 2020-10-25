#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_10_多继承的使用注意事项.py
@time: 2020-10-24 17:58

"""


class A:

    def test(self):
        print("A -- test method")

    def demo(self):
        print("A -- demo method")


class B:
    def test(self):
        print("B -- test method")

    def demo(self):
        print("B -- demo method")


class C(B, A):
    """多继承可以让子类对象同时具有多个父类的属性和方法"""
    pass


# 创建C类对象
c = C()
c.test()
c.demo()

# 确定C类对象调用方法的顺序
print(C.__mro__)