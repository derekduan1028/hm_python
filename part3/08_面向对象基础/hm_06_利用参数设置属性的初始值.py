#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_06_利用参数设置属性的初始值.py
@time: 2020-10-09 15:47

"""


class Cat:
    """这是一个猫类"""

    def __init__(self, vName):
        print("这是一个初始化方法")
        self.name = vName

    def eat(self):
        print("%s爱吃鱼" % self.name)


# 使用类名()创建对象的时候，会自动调用初始化方法 __init__
tom = Cat("Tom")
tom.eat()
lazy_cat = Cat("大懒猫")
lazy_cat.eat()
