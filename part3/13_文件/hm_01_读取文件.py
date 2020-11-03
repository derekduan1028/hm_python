#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_01_读取文件.py
@time: 2020-10-30 11:39

"""

# 1. 打开 —— 文件名需要注意大小写
file = open("README")
# 2. 读取文件内容
text = file.read()
print(text)
# 3. 关闭文件
file.close()

