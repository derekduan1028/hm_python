#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_10_导入包.py
@time: 2020-10-30 08:59

"""

import hm_message
hm_message.send_message.send("OK")
txt = hm_message.receive_message.receive()
print(txt)

