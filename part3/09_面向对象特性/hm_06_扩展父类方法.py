#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_06_扩展父类方法.py
@time: 2020-10-22 10:03

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
        # 1.针对子类特有的需求，编写代码
        print("叫的跟神一样。。。")
        # 2.使用super.()调用原本父类中封装的方法
        super().bark()
        # 使用 父类名.方法名(self)调用父类的方法，
        # 但父类名称写错，容易出现递归调用，造成死循环
        # Dog.bark(self)
        # 3.增加其他子类代码
        print("^%^%^%^%")


xtq = XiaoTianQuan()

# 如果子类中，重写了父类的方法
# 在使用子类对象调用方法时，会调用子类中重写的方法
xtq.bark()
