# -*- coding: utf-8 -*- 
"""
Project: PyLib
Author: Jarod
Create time: 2020-04-10 10:55
IDE: PyCharm
Introduction:
"""

try:
    num = eval(input("请输入："))
    print(num**2)
except:
    print("输入的不是整数！")
