#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_20_for语法演练.py
@time: 11/16/20 2:43 PM

"""

for num in [1,2,3]:
    print(num)
    if num == 2:
        break
else:
    # 如果循环体内部使用break退出了循环
    # else 下方的代码就不会被执行
    print("会执行么")
print("循环结束")
