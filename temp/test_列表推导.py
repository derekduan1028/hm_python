#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: test_列表推导.py
@time: 11/17/20 8:56 AM

"""
import timeit
import time


fooo = """
# Creating our animal park
animal_park = ['Rabbit', 'Rabbit', 'Rabbit', 'Rabbit', 'Cat', 'Cat', 'Cat', 'Cat', 'Cat', 'Cat', 'Cat', 'Turtle',
               'Turtle', 'Turtle', 'Turtle', 'Turtle', 'Turtle', 'Turtle', 'Dog', 'Dog', 'Kangaroo', 'Kangaroo',
               'Kangaroo', 'Kangaroo', 'Kangaroo', 'Kangaroo']

# Creating a new list for our animal doctor with all animals


animal_doctor = []
for animal in animal_park:
    animal_doctor.append(animal)
# print(animal_doctor)
"""

print(timeit.timeit(stmt=fooo, number=10000))


t0 = time.time()
# Creating our animal park
animal_park = ['Rabbit', 'Rabbit', 'Rabbit', 'Rabbit', 'Cat', 'Cat', 'Cat', 'Cat', 'Cat', 'Cat', 'Cat', 'Turtle',
               'Turtle', 'Turtle', 'Turtle', 'Turtle', 'Turtle', 'Turtle', 'Dog', 'Dog', 'Kangaroo', 'Kangaroo',
               'Kangaroo', 'Kangaroo', 'Kangaroo', 'Kangaroo']

# Creating a new list for our animal doctor with all animals


animal_doctor = []
for animal in animal_park:
    animal_doctor.append(animal)
# print(animal_doctor)

t1 = time.time()
total = t1 - t0
print("total: %d 微秒" %(total * 1000000))