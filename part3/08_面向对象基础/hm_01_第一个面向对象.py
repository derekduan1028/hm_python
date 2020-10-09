#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_01_第一个面向对象.py
@time: 2020-10-07 09:43

"""

# lesson 301
class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


Tom = Cat()
Tom.eat()
Tom.drink()

# lesson302
print(Tom)

addr: int = id(Tom)
print("%x" % addr)
print("%d" % addr)