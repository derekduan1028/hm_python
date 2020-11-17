#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_02_判断年龄改进版.py
@time: 2020-11-07 16:17

"""


# 1. 输入用户年龄
age = int(input("请输入你的年龄："))

# 2. 判断是否满18岁
if age >= 18:
    # 3. 如果满了18岁，可以进网吧
    print("已经成年，欢迎进网吧")
else:
    # 4. 如果未满18岁，提示回家写作业
    print("回家写作业")

# 这句代码无论条件成立，都会执行
print("这句代码什么时候执行")

