#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_07_火车站安检.py
@time: 2020-11-08 19:26

"""

# 1. 定义布尔型变量 `has_ticket` 表示是否有车票
has_ticket = True
# 2. 定义整型变量 `knife_length` 表示到的长度，单位：厘米
knife_length = 20
# 3. 首先检查是否有车票，如果有，允许进行 **安检**
if has_ticket:
    print("车票检查通过，准备开始安检")
    # 4. 安检时，需要检查刀的长度，判断是否超过20cm
    if knife_length > 20:
        # 如果超过20厘米，提示刀的长度，不允许上车
        print("刀的长度：%d, 不允许上车" % knife_length)
        # 如果不超过20厘米，安检通过
    else:
        print("安检通过！")
# 5. 如果没有车票，不允许进门
else:
    print("请先买票")



