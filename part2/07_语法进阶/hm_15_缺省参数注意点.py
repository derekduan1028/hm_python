#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_15_缺省参数注意点.py
@time: 11/19/20 4:45 PM

"""


def print_info(name, title="", gender=True):
    """

    :param title: 职位
    :param name: 学生姓名
    :param gender: True：男生，False：女生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("[%s] %s 是 %s" % (title, name, gender_text))


print_info("小明")
print_info("小美", gender=False)
