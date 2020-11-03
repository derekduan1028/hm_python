#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_18__new__方法.py
@time: 2020-10-27 10:52

"""


class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        # 1.使用类名创建对象时，new方法会被自动调用
        print("创建对象，分配空间")
        # 2.为对象分配空间
        instance = super().__new__(cls)
        # 3.返回对象的引用
        return instance

    def __init__(self):
        print("播放器初始化")


# 创建播放器对象
player = MusicPlayer()

print(player)
