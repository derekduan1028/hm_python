#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_11_多态案例.py
@time: 2020-10-24 22:27

"""


class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳。。。" % self.name)


class XiaoTianDog(Dog):

    def game(self):
        print("%s 飞到天上去玩耍" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍" % (self.name, dog.name))
        # 让狗玩耍
        dog.game()


# 创建一个狗对象
# wangcai = Dog("旺财")
wangcai = XiaoTianDog("飞天旺财")
# 创建人的对象
xiaoming = Person("小明")

# 小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)

