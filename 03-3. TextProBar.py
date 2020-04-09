# -*- coding: utf-8 -*- 
"""
Project: PyLib
Author: Jarod
Create time: 2020-04-09 17:59
IDE: PyCharm
Introduction:
"""

import time
'''
for i in range(101):
    print("\r{:3}".format(i), end="%")
    time.sleep(0.1)
'''
scale = 50
print("开始".center(scale//2, "-"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur), end="")
    time.sleep(0.1)
print("\n"+"结束".center(scale//2, "-"))
