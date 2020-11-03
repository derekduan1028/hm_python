#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_04_完整的异常语法.py
@time: 2020-10-28 14:41

"""

try:
    # 1. 提示用户输入一个整数
    num = int(input("请输入一个整数："))

    # 2. 使用`8`除以用户输入的整数并且输出
    result = 8 / num
    # if result == 0:
    print("输入的整数是 [%d]" % result)
except ZeroDivisionError:
    print("除0错误")
except ValueError:
    print("非数字错误")
except Exception as err:
    print("未知错误 [%s]" % err)
else:
    print("尝试成功！")
finally:
    print("无论是否出现错误都会执行！")

print("-" * 50)

