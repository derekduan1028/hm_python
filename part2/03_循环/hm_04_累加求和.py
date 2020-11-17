#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_04_累加求和.py
@time: 2020-11-09 10:50

"""


# 计算 0～100 之间所有数字的累计求和结果


# 定义最终结果的变量
result = 0
# 定义整数变量记录循环次数
i = 0


# 开始循环
while i <= 100:
    # 每一次循环，都让result 这个变量和i这个变量计数器相加
    result = result + i

    # 处理计数器
    i += 1

print("0～%d 之间的数字求和结果 = %d" % (i-1, result))


