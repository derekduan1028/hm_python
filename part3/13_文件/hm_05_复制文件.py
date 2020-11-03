#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_05_复制文件.py
@time: 2020-11-02 11:29

"""
# 1.打开
source_file = open("README1")
target_file = open("README2", "w")
# 2.读、写
text = source_file.read()
target_file.write(text)

# 3.关闭文件
source_file.close()
target_file.close()