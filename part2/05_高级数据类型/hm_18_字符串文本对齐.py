#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_18_字符串文本对齐.py
@time: 11/15/20 4:31 PM

"""

# 要求，顺序并且居中对齐输出
poem = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流\t\n",
        "欲穷千里目",
        "更上一层楼"
]

# 居中对齐
for poem_str in poem:
    print("|%s|" % poem_str.strip().center(10, " "))

print("-" * 50)
# 向左对齐
for poem_str in poem:
    print("|%s|" % poem_str.strip().ljust(10, " "))
