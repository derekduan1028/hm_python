#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_11_temp.py
@time: 2020-10-12 20:49

"""


class House:
    def __init__(self, vHouseType, vArea):
        self.housetype = vHouseType
        self.area = vArea
        # 剩余面积
        self.free_area = self.area
        # 家具列表
        self.item_list = []

    def __str__(self):
        return "房子户型%s，剩余面积%.1f,家具%s" % \
        (self.housetype, self.free_area, self.item_list)

    def add_item(self, vItem):
        self.item_list.append(vItem)
        # print(self.item_list)
        self.free_area = self.area - vItem.area


class HouseItem:
    def __init__(self, vName, vArea):
        self.name = vName
        self.area = vArea

    def __str__(self):
        return "%s 的面积是 %.1f平米" % (self.name, self.area)


# 生成家具
bed = HouseItem("ximengsi", 4.0)
print(bed)
chest = HouseItem("衣柜", 2.0)
print(chest)
table = HouseItem("餐桌", 1.5)
print(table)

# 生成房子
House1 = House("两居室", 50.0)
print(House1)
# 添加家具
House1.add_item(bed)
print(House1)
