#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_01_列表基本使用.py
@time: 2020-11-12 09:43

"""

name_list = ["zhangsan", "lisi", "wangwu"]
# 取值和索引
# list index out range —— 列表索引超出范围
print(name_list[0])
# 使用index方法需要注意，传递的数据不在列表中，程序报错
print(name_list.index("lisi"))
# 修改
name_list[1] = "李四"
# IndexError: list assignment index out of range
# 列表指定的索引超出范围就会报错
# name_list[3] = "wangxiaoer"

# 增加
# append 方法可以向列表的末尾追加数据
name_list.append("王小二")
# insert方法可以在列表的指定索引位置插入数据
name_list.insert(1, "小美")
# extend 可以把其他列表追加到列表的末尾
temp_lst = ["孙悟空", "猪八戒", "沙师弟"]
name_list.extend(temp_lst)

# 删除
# remove 方法可以从列表中删除指定数据
name_list.remove("wangwu")
# pop方法默认可以把列表中最后一个元素删除
name_list.pop()
# pop方法可以指定要删除元素的索引
name_list.pop(3)
# clear方法可以清空整个列表
name_list.clear()

print(name_list)


