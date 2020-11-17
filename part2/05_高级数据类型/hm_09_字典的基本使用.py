#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_09_字典的基本使用.py
@time: 2020-11-13 14:32

"""

xiaoming_dict = {"name": "小明"}


# 取值
print(xiaoming_dict["name"])

# 增加/修改
# 如果key不存在，会新增键值对
xiaoming_dict["age"] = 18
# 如果key存在，会修改已经存在的键值对
xiaoming_dict["name"] = "小小明"

# 删除
# 删除指定键值对时，指定的key不存在，程序报错
xiaoming_dict.pop("name")

print(xiaoming_dict)
