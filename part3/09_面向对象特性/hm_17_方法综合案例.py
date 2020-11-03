#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_17_方法综合案例.py
@time: 2020-10-27 09:59

"""


class Game(object):
    # 定义类属性历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息：XXXX")

    @classmethod
    def show_top_score(cls):
        print("历史记录：%d" % cls.top_score)

    def start_game(self):
        print("%s 开始游戏..." % self.player_name)


# 1. 查看游戏帮助信息
Game.show_help()

# 2. 查看历史最高分
Game.show_top_score()

# 3. 创建游戏对象
game1 = Game("小明")
game1.start_game()






