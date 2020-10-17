#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_15_士兵突击_02_士兵类.py
@time: 2020-10-16 15:23

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


class Soldier:
    def __init__(self, name):
        # 姓名
        self.name = name
        # 枪--新兵没有枪
        self.gun = None


# 创建枪对象
ak47 = Gun("ak47")
ak47.add_bullet(50)
ak47.shoot()

# 创建士兵
xusanduo = Soldier("xusanduo")

# 给对象属性赋值，属性已经在类内部定义，初始值None
xusanduo.gun = ak47
print(xusanduo.gun)
