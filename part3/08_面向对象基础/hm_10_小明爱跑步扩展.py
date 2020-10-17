#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_10_小明爱跑步扩展.py
@time: 2020-10-12 14:19

"""

class Person:
    def __init__(self, name, weight):
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫%s,体重是 %.2f" % (self.name, self.weight)

    def run(self):
        print("%s爱跑步" % self.name)
        self.weight -= 0.5
    def eat(self):
        print("%s是吃货" % self.name)
        self.weight += 1


xiaoming = Person("xiaoming", 75.0)

xiaoming.run()
xiaoming.eat()
print(xiaoming)

# xiaomei

xiaomei = Person("xiaomei", 45.0)
xiaomei.eat()
xiaomei.run()
print(xiaomei)
