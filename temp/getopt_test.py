#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: getopt_test.py
@time: 2020-09-28 15:21

"""

from getopt import getopt
import sys
opts, args = getopt.getopt(sys.argv[1:], "ho:", ["help", "output="])

print(opts)
print(args)