#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_02_第一个while循环.py
@time: 2020-11-08 22:38

"""

# 打印5遍 hello python
# 定义重复次数计数器
i = 1

# 使用while 判断条件
while i <= 5:
    # 循环内执行的代码
    print("hello python")
    # 处理计数器
    i += 1
print("循环结束后的 i = %d" % i)

