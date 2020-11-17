#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_07_元组遍历.py
@time: 2020-11-13 11:12

"""

info_tuple = ("zhangsan", 18, 1.75)

# 使用迭代遍历元组
for my_info in info_tuple:
    # 使用格式字符串拼接my_info并不方便，因为变量类型不同
    print(my_info)
