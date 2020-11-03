#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_06_from_import_注意事项.py
@time: 2020-10-29 11:18

"""


from hm_01_测试模块1 import say_hello
from hm_02_测试模块2 import say_hello as module2_say_hello

say_hello()
module2_say_hello()
