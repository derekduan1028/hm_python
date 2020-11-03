#!/usr/bin/python
#coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: hm_03_import导入模块.py
@time: 2020-10-28 17:16

"""
# 测试模块需放在项目的根目录下？放在11_模块中无法找到

import hm_01_测试模块1 as DogModule
import hm_02_测试模块2 as CatModule
import module1 as mod1

print(DogModule.__file__)
print(CatModule.__file__)
print(mod1.__file__)

DogModule.say_hello()
CatModule.say_hello()

dog = DogModule.Dog()
print(dog)

cat = CatModule.Cat()
print(cat)
