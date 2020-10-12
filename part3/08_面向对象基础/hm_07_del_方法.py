#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_07_del_方法.py
@time: 2020-10-10 09:57

"""

class Cat:
    def __init__(self,vName):
        self.name = vName

    def eat(self):
        print("%s爱吃鱼" % self.name)

    def __del__(self):
        print("%s 离开了" % self.name)


tom = Cat("Tom")

print(tom)
tom.eat()

# del关键字可以删除对象，这样删除会在线上执行
# del tom

# 全局变量，会在下面这行代码执行后才销毁
print("-" * 50)