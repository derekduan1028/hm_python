#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: lxy.py
@time: 2020-10-21 15:02

"""

import matplotlib.pyplot as plt
import numpy as np


def lxy(x, y):
    n = len(x)
    sum_x = 0
    sum_y = 0
    total = 0
    for i in range(0,n):
        sum_x = sum_x + x[i]
        sum_y = sum_y + y[i]
        total = total + x[i]*y[i]
    return total - sum_x*sum_y/n


if __name__ == "__main__":
    w = [57, 64, 41, 38, 35, 44, 41, 51, 57, 49, 47, 46]
    h = [171, 175, 159, 155, 152, 158, 154, 164, 168, 166, 159, 164]
    # plt.scatter(h, w)
    # plt.show
    b = lxy(h, w) / lxy(h, h)
    print("b is %.4f" % b)
    a = np.mean(w) - b * np.mean(h)
    print("a is %.4f" % a)







