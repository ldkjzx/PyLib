# -*- coding: utf-8 -*- 
"""
Project: PyLib
Author: Jarod
Create time: 2020-04-01 16:15
IDE: PyCharm
Introduction:
"""

import turtle

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


turtle.setup(650, 350, 200, 200) # 设置窗口大小，和屏幕绝对位置
turtle.penup() # 画笔抬起，海龟飞行
turtle.fd(-250) # 海龟从原点移动
turtle.pendown() # 画笔放下，海龟爬行
turtle.pensize(25) # 海龟腰围
turtle.pencolor("purple") # 海龟颜色
turtle.seth(-40) # 设置海龟绝对角度
for i in range(4):
    turtle.circle(40, 80) # 海龟曲线前进，r + 弧度
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40) # 海龟直线前进
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()





