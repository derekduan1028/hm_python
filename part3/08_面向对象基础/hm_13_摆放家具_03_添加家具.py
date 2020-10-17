#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_13_摆放家具_03_添加家具.py
@time: 2020-10-15 18:08

"""


class HouseItem:
    def __init__(self, vName, vArea):
        self.name = vName
        self.area = vArea

    def __str__(self):
        return "[%s] 占地面积是 [%.1f]平米" % (self.name, self.area)


class House:
    def __init__(self, vHouseType, vArea):
        self.housetype = vHouseType
        self.area = vArea
        # 剩余面积
        self.free_area = self.area
        # 家具列表
        self.item_list = []

    def __str__(self):
        # python能够自动将一对括号内部的代码连接在一起
        return ("户型：%s\n面积：%.2f[剩余面积%.1f]\n家具:%s"
        % (self.housetype, self.area, self.free_area, self.item_list))

    def add_item(self, vItem):
        print("要添加%s\n" % vItem)
        # 判断家具的面积
        if vItem.area > self.free_area:
            print("%s 的面积太大，无法添加" % vItem.name)
            return
        # 将家具的名称添加到列表中
        self.item_list.append(vItem.name)
        # 计算剩余面积
        self.free_area -= vItem.area


# 1.生成家具
bed = HouseItem("席梦思", 40.0)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
# print(bed)
# print(chest)
# print(table)

# 2.创建房子对象
my_home = House("两居室", 60)

# 3.添加家具
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)
