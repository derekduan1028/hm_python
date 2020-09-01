#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: test1.py
@time: 2020-08-31 11:27

"""
import subprocess
comd = "cd /Users/derek;cat test1.py.txt"
b = subprocess.call([comd], shell=True)
print(b)


