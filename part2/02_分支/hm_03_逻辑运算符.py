#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_03_逻辑运算符.py
@time: 2020-11-07 17:51

"""


# 练习1: 定义一个整数变量 `age` , 编写代码判断年龄是否正确
age = 12

# 要求人的年龄在0-120 之间
if 0 <= age <= 120:
    print("年龄正确")
else:
    print("年龄不正确")

# 练习2: 定义两个整数变量 `Python_score` \ `c_score` , 编写代码判断成绩
python_score = 80
c_score = 6
# 要求只要有一门成绩 >60 分就算合格
if python_score > 60 or c_score > 60:
    print("考试合格")
else:
    print("不及格")

# 练习3: 定义一个布尔型变量 `is_employee`, 编写代码判断是否是本公司员工
is_employee = False

# 如果不是提示不允许入内
if not is_employee:
    print("非本公司员工，禁止入内")


