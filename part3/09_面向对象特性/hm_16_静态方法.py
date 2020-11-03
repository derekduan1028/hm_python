#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_16_静态方法.py
@time: 2020-10-26 14:49

"""


class Dog(object):

    @staticmethod
    def run():
        # 不访问 实例属性/类属性
        print("小狗要跑")

    def __init__(self, name):
        self.name = name


# 通过 类名. 的方式调用静态方法 - 不需要创建对象
Dog.run()


