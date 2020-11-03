#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_19_单例.py
@time: 2020-10-27 11:32

"""


class MusicPlayer(object):
    # 定义类属性，记录第一个单例对象的引用
    instance = None

    def __new__(cls, *args, **kwargs):
        # 判断类属性是否是空对象
        if cls.instance is None:
            # 调用父类方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 返回保存的类属性对象引用
        return cls.instance

    def __init__(self):
        print("初始化")


# 创建三次实例，查看引用是否相同
for i in range(3):
    player1 = MusicPlayer()
    print("第[%d]次: %s" % (i + 1, player1))
