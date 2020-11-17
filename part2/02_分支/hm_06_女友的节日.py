#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_06_女友的节日.py
@time: 2020-11-07 22:13

"""


# 1. 定义 `holiday_name` 字符串变脸记录节日名称
holiday_name = "妇女节"
# 2. 如果是 **情人节** 应该 **买玫瑰/看电影**
if holiday_name == "情人节":
    print("买玫瑰，看电影")
# 3. 如果是 **平安夜** 应该 **买苹果/吃大餐**
elif holiday_name == "平安夜":
    print("买苹果,吃大餐")
# 4. 如果是 **生日** 应该 **买蛋糕**
elif holiday_name == "生日":
    print("买蛋糕")
# 5. 其他的日子每天都是节日啊...
else:
    print("每天都是节日啊")

