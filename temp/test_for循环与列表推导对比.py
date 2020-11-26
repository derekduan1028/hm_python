#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: test_for循环与列表推导对比.py
@time: 11/19/20 3:40 PM

"""

import timeit
fooo = """
sum = []
for i in range(1000):
    sum.append(i)
"""


print(timeit.timeit(stmt="[i for i in range(1000)]", number=100000))
print(timeit.timeit(stmt=fooo, number=100000))
