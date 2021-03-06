#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_08_父类的公有方法.py
@time: 2020-10-22 15:59

"""

class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))

    def test(self):
        print("父类的公有方法 %d" % self.__num2)
        self.__test()


class B(A):
    def demo(self):
        # 1.访问父类的私有属性
        # print("访问父类的私有属性 %d" % self.__num2)
        # 2.子类对象中，不能调用父类的私有方法
        # self.__test()
        # 3.访问父类的公有属性
        print("子类方法 %d" % self.num1)
        # 4.调用父类的公有方法
        self.test()


# 创建子类对象
b = B()
print(b)

b.demo()
b.test()
# 在外界访问父类的公有属性和公有方法
# print(b.num1)
# b.test()

# 外界不能直接访问对象的私有属性，调用私有方法
# print(b.__num2)
# b.__test()
