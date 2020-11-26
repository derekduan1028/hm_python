#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_18_元组和字典的拆包.py
@time: 11/20/20 10:29 AM

"""


def demo(*args, **kwargs):
    print(args)
    print(kwargs)


# 元组变量或者字典变量直接传递给函数时
gl_nums = (1, 2, 3)
gl_dict = {"name": "小明", "age": 18}

# 拆包语法，简化传递
demo(*gl_nums, **gl_dict)
