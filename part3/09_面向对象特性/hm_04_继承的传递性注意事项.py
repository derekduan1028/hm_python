#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_04_继承的传递性注意事项.py
@time: 2020-10-17 17:15

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


class Cat(Animal):
    def catch(self):
        print("抓老鼠")


# 创建一个啸天犬对象
xtq = XiaoTianQuan()

xtq.fly()
xtq.bark()
xtq.eat()

xtq.catch()

