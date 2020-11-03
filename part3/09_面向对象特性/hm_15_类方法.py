#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_15_类方法.py
@time: 2020-10-26 10:07

"""


class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    @classmethod
    def show_tool_count(cls):
        # 现实工具对象的总数
        print("工具对象的数量：%d" % cls.count)

    def __init__(self, name):
        self.name = name
        # 让类属性+1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")
# 调用类方法
Tool.show_tool_count()
