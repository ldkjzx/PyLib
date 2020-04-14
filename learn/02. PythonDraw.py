# -*- coding: utf-8 -*- 
"""
Project: PyLib
Author: Jarod
Create time: 2020-04-01 16:15
IDE: PyCharm
Introduction:
"""

# import turtle         # 无库名冲突，但代码冗余
# from turtle import *   # 易产生库名冲突
import turtle as t  # 库别名

# 海龟角度坐标
'''
turtle.left(45)
turtle.fd(150)
turtle.right(135)
turtle.fd(300)
turtle.left(135)
turtle.fd(150)
'''

# 海龟空间坐标
'''
turtle.goto( 100, 100)
turtle.goto( 100,-100)
turtle.goto(-100,-100)
turtle.goto(-100, 100)
turtle.goto(0,0)
'''

t.setup(650, 350, 200, 200)  # 设置窗口大小，和屏幕绝对位置
t.pu()  # 画笔抬起，海龟飞行
t.fd(-250)  # 海龟从原点移动
t.pd()  # 画笔放下，海龟爬行
t.pensize(25)  # 海龟腰围
t.pencolor("purple")  # 海龟颜色
t.seth(-40)  # 设置海龟绝对角度
for i in range(4):
    t.circle(40, 80)  # 海龟曲线前进，r + 弧度
    t.circle(-40, 80)
t.circle(40, 80 / 2)
t.fd(40)  # 海龟直线前进
t.circle(16, 180)
t.fd(40 * 2 / 3)
t.done()
