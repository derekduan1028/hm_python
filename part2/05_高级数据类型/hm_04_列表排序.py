#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_04_列表排序.py
@time: 2020-11-12 14:27

"""

name_list = ["zhangsan", "lisi", "wangwu", "wangxiaoer"]
num_list = [6, 8, 4, 1, 10]


# 升序
# name_list.sort()
# num_list.sort()
# 降序
# name_list.sort(reverse=True)
# num_list.sort(reverse=True)
# 逆序（反转）
name_list.reverse()
num_list.reverse()

print(name_list)
print(num_list)
