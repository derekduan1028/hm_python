#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_09_格式化输出.py
@time: 2020-11-06 15:31

"""

# 定义字符串变量 name ，输出 我的名字叫 小明，请多多关照
name = "小明"
print("我的名字叫 %s，请多多关照" % name)

# 定义整数变量 student_no, 输出 我的学号是 000001
student_no = 1
print("我的学号是 %06d" % student_no)

# 定义小数price weight money，
# 输出 苹果单价 9.00元/斤，购买了 5.00斤, 需要支付 45.00元
price = 9.0
weight = 5.0
money = price * weight
print("苹果单价 %.02f元/斤 购买了 %.02f斤, 需要支付 %.04f元"
      % (price, weight, money))

# 定义了一个小数 scale，输出 数据比例是 10.00%
scale = 0.25
print("数据比例是 %.2f%%" % (scale * 100))
