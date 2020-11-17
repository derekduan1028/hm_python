#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_02_del关键字.py
@time: 2020-11-12 11:03

"""


name_list = ["张三", "李四", "王五"]

# 使用 del关键字 删除列表元素
# 建议使用列表方法，pop或者remove
del name_list[1]
# del 关键字本质上是用来将一个变量从内存中删除的

print(name_list)

