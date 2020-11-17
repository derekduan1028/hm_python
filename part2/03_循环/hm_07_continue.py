#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_07_continue.py
@time: 2020-11-09 14:07

"""

i = 0
while i < 10:
    # continue 某一条件满足时，不执行后续重复的代码
    if i == 3:
        # 使用continue，需要确认循环的计数是否修改，否则导致死循环
        i += 1
        continue
    print(i)
    i += 1

print("over")