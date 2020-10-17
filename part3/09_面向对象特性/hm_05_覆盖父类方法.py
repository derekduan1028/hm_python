#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_05_覆盖父类方法.py
@time: 2020-10-17 17:37

"""


class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("i can fly!")
    def bark(self):
        print("叫的跟神一样。。。")


xtq = XiaoTianQuan()

# 如果子类中，重写了父类的方法
# 在使用子类对象调用方法时，会调用子类中重写的方法
xtq.bark()



