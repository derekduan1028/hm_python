#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_04_在外界设置属性的问题.py
@time: 2020-10-08 21:12

"""

class Cat:
    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
Tom = Cat()

Tom.eat()
Tom.drink()

# 利用 .属性名 赋值语句设置变量属性（不推荐）
Tom.name = "tom"

print(Tom)