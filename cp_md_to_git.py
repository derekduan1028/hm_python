#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: cp_md_to_git.py
@time: 2020-11-03 11:00

"""

# 打开文件
md_file = open("/Users/derek/Desktop/笔记/hm-笔记/hm-python.md")
md_file_git = open("/Users/derek/PycharmProjects/hm_python/hm-python.md", 'w')
# 复制文件
while True:
    text = md_file.readline()
    if not text:
        break
    md_file_git.write(text)
# 关闭文件
md_file.close()
md_file_git.close()

