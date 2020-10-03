#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: parse_1.py
@time: 2020-09-27 15:08

"""

from parse import *

url = "https://act-m.wandafilm.com/1708/8173/?cinemaCode=288"
result = parse('https://{host}/1708/8173/?cinemaCode={cinemaCode}', \
               url)
print(result["cinemaCode"])
print(result["host"])
