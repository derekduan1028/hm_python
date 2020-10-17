#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_17_私有属性和方法.py
@time: 2020-10-17 09:36

"""


class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 [%d]" % (self.name, self.__age))


xiaofang = Women("小芳")
# 私有属性，在外界不能够被直接访问
# print(xiaofang.__age)
# 私有方法，同样不允许在外界被直接访问
# xiaofang.__secret()
