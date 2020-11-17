#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_05_偶数求和.py
@time: 2020-11-09 11:05

"""

# 1. 编写循环 确认 要计算的数字
# 2. 添加 结果 变量，在循环内部 处理计算结果


# 定义最终结果的变量
result = 0
# 定义整数变量记录循环次数
i = 0


# 开始循环
while i <= 100:
    # 判断变量i中的数值，是否是偶数
    if i % 2 == 0:
        print(i)
        # 每一次循环，都让result 这个变量和i这个变量计数器相加
        result = result + i

    # 处理计数器
    i += 1

print("0～%d 之间的偶数求和结果 = %d" % (i-1, result))

