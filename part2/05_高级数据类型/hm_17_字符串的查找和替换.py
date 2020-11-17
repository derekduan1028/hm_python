#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_17_字符串的查找和替换.py
@time: 11/15/20 12:28 PM

"""


hello_str = "hello world"

# 1. 判断是否以指定字符串开始
print(hello_str.startswith("hello"))

# 2. 判断是否以指定字符串结束
print(hello_str.endswith("world"))

# 3. 查找字符串
# 类似index,查找指定的字符串在大字符串中的索引
# 如果查找的字符串不存在，find不会报错，而是返回 -1
print(hello_str.find("llo"))
print(hello_str.find("abc"))

# 4. 替换字符串
# replace 方法执行完成后，会返回一个新的字符串
# 注意：不会修改原字符串
print(hello_str.replace("world", "python"))
print(hello_str)


