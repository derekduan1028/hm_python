#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_08_石头剪刀布.py
@time: 2020-11-08 19:43

"""

import random
2
lst = ["石头", "剪刀", "布"]
# 1. 从控制台输入要出的拳 —— 石头（1）/剪刀（2）/布（3）
player = int(input("请出拳 石头（1）/剪刀（2）/布（3）："))

# 2. 电脑随机出拳 —— 先假定电脑只会出石头，完成整体代码
computer = random.randint(1, 3)
print("玩家: %s —— 计算机: %s" % (lst[player - 1], lst[computer - 1]))
# 3. 比较胜负
# 1 石头 胜 剪刀
# # 2 剪刀 胜 布
# # 3 布 胜 石头
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("玩家胜利")
elif player == computer:
    print("平局")
else:
    print("电脑胜利，再来一盘")
