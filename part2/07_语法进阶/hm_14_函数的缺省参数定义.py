#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_14_函数的缺省参数定义.py
@time: 11/19/20 3:20 PM

"""


def print_info(name,gender=True):
    """

    :param name: 学生姓名
    :param gender: True：男生，False：女生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s 是 %s" % (name, gender_text))


print_info("小明", True)

