# -*- coding: utf-8 -*- 
"""
Project: PyLib
Author: Jarod
Create time: 2020-04-10 10:55
IDE: PyCharm
Introduction:
"""

'''
try:
    guess = eval(input("请输入："))
    print("猜{}了！".format("对对" if guess==99 else "错错"))


    #if guess>99 or guess<99:
    #    print("猜错了！")
    #else:
    #    print("猜对了！")

except:
    print("输入的不是整数！")
'''

score = eval(input())
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
print("输入成绩属于级别{}".format(grade))
