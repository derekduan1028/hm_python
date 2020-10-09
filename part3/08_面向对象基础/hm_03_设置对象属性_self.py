#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_03_设置对象属性_self.py
@time: 2020-10-08 17:50

"""


class Cat:
    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
Tom = Cat()
# 利用 .属性名 赋值语句设置变量属性（不推荐）
Tom.name = "tom"

Tom.eat()
Tom.drink()

print(Tom)

# 再创建一个猫对象
lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)