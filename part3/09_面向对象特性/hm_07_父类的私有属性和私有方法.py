#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_07_父类的私有属性和私有方法.py
@time: 2020-10-22 15:45

"""


class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))


class B(A):
    def demo(self):
        # 访问父类的私有属性
        # print("访问父类的私有属性 %d" % self.__num2)
        # 子类对象中，不能调用父类的私有方法
        # self.__test()
        pass


# 创建子类对象
b = B()
print(b)

b.demo()


# 外界不能直接访问对象的私有属性，调用私有方法
# print(b.__num2)
# b.__test()
