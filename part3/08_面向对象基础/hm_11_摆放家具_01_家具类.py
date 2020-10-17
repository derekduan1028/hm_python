#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_11_摆放家具_01_家具类.py
@time: 2020-10-13 10:35

"""


class HouseItem:
    def __init__(self, vName, vArea):
        self.name = vName
        self.area = vArea

    def __str__(self):
        return "[%s] 占地面积是 [%.1f]平米" % (self.name, self.area)


# 生成家具
bed = HouseItem("席梦思", 4.0)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
print(bed)
print(chest)
print(table)

