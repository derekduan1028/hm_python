#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_06_元组基本操作.py
@time: 2020-11-13 11:01

"""


info_tuple = ("zhangsan", 18, 1.75, "zhangsan")

# 取值和索引
print(info_tuple[0])
# 已经知道数据的内容，希望知道数据的索引
print(info_tuple.index(1.75))

# 统计计数
count = info_tuple.count("zhangsan")
print(count)

# 统计元组中包含的元素个数
print(len(info_tuple))
