#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_09_小明爱跑步.py
@time: 2020-10-10 11:39

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

