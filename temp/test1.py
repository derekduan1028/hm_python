#!/usr/bin/python
# coding:utf-8

"""

@author:derek
@contract:derek_duan@sina.com
@file: test1.py
@time: 2020-08-31 11:27

"""
import subprocess

comd = "cd /Users/derek;cat test1.py.txt"
subprocess.call([comd], shell=True)
print("getoutput:**********************")
comd2 = "ls /Users/derek"
a = subprocess.getoutput([comd2])
print(type(a))
c = a.split("\n")
print(c, type(c))

gl_list = []
# print(gl_list.__dir__())
print(dir(gl_list))
print(dir(1))


def demo():
    """this is a demo function"""
    print("hello world!")


if __name__ == "__main__":
    var = demo.__doc__
    print(var)

# b=[]
# for i in a:
#     b.append(i)
# print(b)


<img src="Users/derek/Library/Application Support/typora-user-images/image-20201105092742335.png" \
    alt="image-20201105092742335.png" style="zoom:80%;" />

<img src="/Users/derek/Library/Application Support/typora-user-images/image-20201019103902279.png" align="left" alt="image-20201019103902279" style="zoom:80%;" />