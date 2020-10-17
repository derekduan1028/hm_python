#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_14_士兵突击_01_枪类.py
@time: 2020-10-16 09:45

"""


class Gun:
    def __init__(self, model):
        # 枪的型号
        self.model = model
        # 子弹的数量
        self.count = 0

    # load bullet
    def add_bullet(self, count):
        self.count += count

    def shoot(self):
        # 判断子弹数量
        if self.count <= 0:
            print("[%s] no bullet , can't fire " % self.model)
            return
        # 发射子弹 -1
        self.count -= 1
        # 提数发射信息
        print("[%s] tututu...[%d]" % (self.model, self.count))

    def __str__(self):
        return "this is a %s,count:[%i]" % (self.model, self.count)


ak47 = Gun("ak47")
ak47.add_bullet(10)
ak47.shoot()

