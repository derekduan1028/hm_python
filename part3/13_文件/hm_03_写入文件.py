#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_03_写入文件.py
@time: 2020-11-02 10:27

"""

# 1.打开文件
file = open("README1", "w")
# 2.写入文件

for i in range(3):
    file.write("第%d行：hello%d" % (i, i+1))
    file.write("\r")
# 3.关闭文件
file.close()

