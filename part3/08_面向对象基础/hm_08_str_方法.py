#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_08_str_方法.py
@time: 2020-10-10 10:28

"""

# !/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_07_del_方法.py
@time: 2020-10-10 09:57

"""


class Cat:
    def __init__(self, vName):
        self.name = vName

    def eat(self):
        print("%s爱吃鱼" % self.name)

    def __del__(self):
        print("%s 离开了" % self.name)

    def __str__(self):
        # 必须返回一个字符串
        return "我是小猫[%s]" % self.name


# tom是一个全局变量
tom = Cat("Tom")
print(tom)
