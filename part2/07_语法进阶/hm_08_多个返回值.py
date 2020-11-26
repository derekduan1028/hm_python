#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_08_多个返回值.py
@time: 11/19/20 9:59 AM

"""


def measure():
    """测量温度和湿度"""
    print("测量开始...")
    temp = 39
    wetness = 50
    print("测量结束...")

    # 返回一个包含多个数据的元组
    return temp, wetness


# 元组
result = measure()
print(result)

# 需要单独处理温度或湿度 - 不方便
print(result[0])
print(result[1])

# 使用多个变量一次接收返回结果
gl_temp, gl_wetness = measure()
print("温度:%d" % gl_temp)
print("湿度:%d" % gl_wetness)
