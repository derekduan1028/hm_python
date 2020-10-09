#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_02_新建两个猫对象.py
@time: 2020-10-08 12:36

"""


# lesson 303
class Cat:
    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
Tom = Cat()

Tom.eat()
Tom.drink()

print(Tom)

# 再创建一个猫对象
lazy_cat = Cat()

lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)

lazy_cat2 = lazy_cat
print(lazy_cat2)

# lesson 304 设置对象属性_self
# 使用 .属性名 利用赋值语句
Tom.name = "Tom"

print(Tom.name)