#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: multi_time_add.py
@time: 2020-09-15 15:24

"""


def time_add(time_1, time_2):
    t1 = time_1.split(":")
    t2 = time_2.split(":")
    h1 = int(t1[0])
    h2 = int(t2[0])
    m1 = int(t1[1])
    m2 = int(t2[1])

    h_jinwei = 0
    m_result = m1 + m2
    h_jinwei = m_result // 60
    h_result = h1 + h2 + h_jinwei
    m_result = m_result - 60 * h_jinwei
    if m_result < 10:
        time_result = ("time result is %s:0%s" % (h_result, m_result))
    else:
        time_result = ("time add result is %s:%s" % (h_result, m_result))
    return time_result


def multi_time_add(time_list):
    h_tmp = 0
    m_tmp = 0
    s_tmp = 0

    for i in time_list:
        time_mem = i.split(":")
        h_tmp = h_tmp + int(time_mem[0])
        m_tmp = m_tmp + int(time_mem[1])
        if len(time_mem) == 3:
            s_tmp = s_tmp + int(time_mem[2])

    time_total = h_tmp * 3600 + m_tmp * 60 + s_tmp
    h_result = time_total // 3600
    m_result = (time_total - 3600 * h_result) // 60
    s_result = time_total - 3600 * h_result - 60 * m_result

    # return h_result, m_result, s_result
    if m_result < 10:
        if s_result < 10:
            time_result = ("time result is %s:0%s:0%s" % (h_result, m_result, s_result))
        else:
            time_result = ("time result is %s:0%s：%s" % (h_result, m_result, s_result))
    else:
        if s_result < 10:
            time_result = ("time add result is %s:%s:0%s" % (h_result, m_result, s_result))
        else:
            time_result = ("time add result is %s:%s:%s" % (h_result, m_result, s_result))
    return time_result


# x = time_add("3:00", "4:14")
# print(x)

var_list = ["7:58", "10:29", "1:28", "7:09", "10:39", "11:17", "8:30"]
y = multi_time_add(var_list)
print(y)
