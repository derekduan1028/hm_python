#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: test_turtle.py
@time: 2020-09-16 15:41

"""

import turtle
import math

bob = turtle.Turtle()
print(bob)


def square(t, vlen, n):
    t.pd()

    for i in range(n):
        t.fd(vlen)
        t.lt(360 / n)
        turtle.mainloop


def circle(t, r):
    square(t, 10, 36)
    circumference = 2 * math.pi * r
    print(circumference)


circle(bob, 4)
turtle.done()



