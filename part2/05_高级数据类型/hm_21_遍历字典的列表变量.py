#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_21_遍历字典的列表变量.py
@time: 11/16/20 2:53 PM

"""


students = [{"name": "阿土"},
            {"name": "小美"}]

find_name = "阿土"

for stu_dict in students:
    # print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了 %s" % find_name)
        break
else:
    # 如果没有找到目标，还希望得到一个提示
    print("抱歉，没有找到 %s" % find_name)
print("循环结束")

