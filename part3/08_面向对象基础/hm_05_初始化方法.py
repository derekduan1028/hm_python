#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_05_初始化方法.py
@time: 2020-10-09 11:17

"""


class Cat:
    """这是一个猫类"""

    def __init__(self):
        print("这是一个初始化方法")
        self.name = "tom"

    def eat(self):
        print("%s爱吃鱼" % self.name)


# 使用类名()创建对象的时候，会自动调用初始化方法 __init__
tom = Cat()
tom.eat()
