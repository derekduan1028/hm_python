#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_03_列表的数据统计.py
@time: 2020-11-12 11:10

"""

name_list = ["张三", "李四", "王五", "张三"]

# len(lenth 长度) 函数可以统计列表中元素的总数
lst_len = len(name_list)
print("列表长度：%d" % lst_len)

# count 方法可以统计列表中某一个数据出现的次数
count = name_list.count("张三")
print("张三出现了 %d 次" % count)

# 从列表中删除首次出现的匹配数据
name_list.remove("张三")

print(name_list)
