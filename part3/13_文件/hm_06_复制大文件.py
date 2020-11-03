#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_06_复制大文件.py
@time: 2020-11-02 11:43

"""

# 1.打开
source_file = open("README1")
target_file = open("README2", "w")
# 2.读、写
while True:
    # 按行读取文件
    text = source_file.readline()
    # 判断是否读取到内容
    if not text:
        break
    target_file.write(text)

# 3.关闭文件
source_file.close()
target_file.close()


