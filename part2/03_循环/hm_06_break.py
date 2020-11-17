#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_06_break.py
@time: 2020-11-09 11:31

"""

i = 0
while i < 10:
    # break 某一条件满足时，退出循环，不再执行后续重复的代码
    if i == 3:
        break
    print(i)
    i += 1

print("over")


