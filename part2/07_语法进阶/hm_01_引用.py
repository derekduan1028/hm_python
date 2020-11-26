#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_01_引用.py
@time: 11/17/20 10:03 AM

"""


def test(num):
    print("函数内部 %d 对应的内存地址是 %d" %(num, id(num)))

    result = "hello"

    print("函数要返回的数据的内存地址是：%d" % id(result))

    # 返回字符串变量
    return result
# 定义一个数字变量
a = 10

# 数据的地址本质上是一个数字
print(" a 变量的内存地址是 %d" % id(a))

# 调用 test 函数，本质上传递的是实参保存数据的引用，而不是实参保存的数据
# 如果函数有返回，但是没有定义变量接收，程序不会报错，无法获得返回结果

r = test(a)
print("%s 的内存地址是：%d" % (r, id(r)))

print("-" * 50)

demo_list = [1, 2, 3]
print("定义列表后的内存地址：%d" % id(demo_list))

demo_list.append(999)
demo_list.pop(0)
demo_list.remove(2)
demo_list[0] = 10

print(demo_list)
print("修改列表后的内存地址：%d" % id(demo_list))

print("-" * 50)
demo_dict = {"name": "小明"}

print("定义字典后的内存地址：%d" % id(demo_dict))

demo_dict["age"] = 18
demo_dict.pop("name")
demo_dict["name"] = "老王"

print(demo_dict)
print("修改字典后的内存地址：%d" % id(demo_dict))