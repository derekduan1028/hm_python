#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_08_模块的搜索顺序.py
@time: 2020-10-29 14:36

"""


import random


print(random.__file__)

for i in range(100):
    rand = random.randint(0, 10)
    print("第%d次：【%d】" % (i+1, rand))


