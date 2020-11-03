#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_20_单例初始化一次.py
@time: 2020-10-27 14:11

"""


class MusicPlayer(object):
    # 定义类属性，记录第一个单例对象的引用
    instance = None
    init_count = 0
    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 判断类属性是否是空对象
        if cls.instance is None:
            # 调用父类方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 返回保存的类属性对象引用
        return cls.instance

    def __init__(self):
        # 判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return
        # 如果没有执行过，执行初始化动作
        print("初始化")
        MusicPlayer.init_count += 1
        # 修改类属性标记
        MusicPlayer.init_flag = True

    @classmethod
    def show_init_times(cls):
        print(cls.init_count)


# 创建三次实例，查看引用是否相同
for i in range(3):
    player1 = MusicPlayer()
    print("第[%d]次创建对象: %s" % (i + 1, player1))

# 查看初始化方法被调用的次数
MusicPlayer.show_init_times()

