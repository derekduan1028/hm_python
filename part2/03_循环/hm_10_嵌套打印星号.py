#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_10_嵌套打印星号.py
@time: 2020-11-09 21:49

"""

# * 在控制台连接输出五行 `*` ，每一行星号的数量依次递增
# *
# **
# ***
# ****
# *****

# 开发步骤
#
# * 1> 完成5行内容的简单输出
# * 2> 分析每行内部的 `*` 应该如果处理

row = 1
while row <= 5:
    # 每一行要打印的星号就是和当前的行数是一致的
    # 增加一个小的循环，专门负责当前行中，每一列的星号显示
    # 定义列的计数器
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    print("")
    row += 1

# 打印圣诞树
row = 1
high = 5
while row <= high:
    # 每一行要打印的星号就是和当前的行数是一致的
    # 增加一个小的循环，专门负责当前行中，每一列的星号显示
    # 定义列的计数器
    col = 1
    print(" " * (high - row), end="")
    while col <= 2 * row - 1:
        print("*", end="")
        col += 1
    print("")
    row += 1
