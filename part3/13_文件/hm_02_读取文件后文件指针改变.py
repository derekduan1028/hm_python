#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_02_读取文件后文件指针改变.py
@time: 2020-11-02 09:57

"""


# 1. 打开 —— 文件名需要注意大小写
file = open("README")
# 2. 读取文件内容
text = file.read()
print(text)
print(len(text))

print("-" * 50)
# 文件指针已移动到文件末尾，不会读取到任何内容
text = file.read()
print(text)
print(len(text))
# 3. 关闭文件
file.close()

