#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_10_字典的其他操作.py
@time: 2020-11-13 14:59

"""

xiaoming_dict = {"name": "小明",
                 "age": 18}

# 统计键值对的数量
print(len(xiaoming_dict))

# 合并字典
tmp_dict = {"height": 1.75,
            "age": 20}
# 注意：被合并字典中包含已存在的键值对时，会覆盖原有的键值对
xiaoming_dict.update(tmp_dict)

# 清空字典
xiaoming_dict.clear()

print(xiaoming_dict)
