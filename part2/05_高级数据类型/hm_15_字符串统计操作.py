#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_15_字符串统计操作.py
@time: 11/14/20 6:37 PM

"""

hello_str = "hello hello"

# 统计字符串长度
print(len(hello_str))

# 统计某一个小字符出现的次数
print(hello_str.count("llo"))
print(hello_str.count("abc"))

# 某一个子字符串出现的位置
print(hello_str.index("llo"))
# 如果index方法传递的子字符串不存在，程序会报错
print(hello_str.index("abc"))