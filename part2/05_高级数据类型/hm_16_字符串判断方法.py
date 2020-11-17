#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_16_字符串判断方法.py
@time: 11/14/20 9:37 PM

"""


# 1. 判断空白字符
space_str = "    \t\n\r"
print(space_str.isspace())

# 2. 判断字符串中只包含数字
# 以下三个方法都不能判断小数
# num_str = "1.1"
# num_str = "\u00b2"
num_str = "一千"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())
