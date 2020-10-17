#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_01_不使用继承开发动物和狗.py
@time: 2020-10-17 15:51

"""


class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

    def bark(self):
        print("汪汪叫")


wangcai = Dog()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()
