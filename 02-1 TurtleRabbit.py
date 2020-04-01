# -*- coding: utf-8 -*- 
"""
Project: PyLib
Author: Jarod
Create time: 2020-04-01 18:39
IDE: PyCharm
Introduction:
"""

import turtle

'''
turtle.setup(800,800,200,200)
turtle.penup()
turtle.goto(189,50)
turtle.pendown()
turtle.pencolor("purple") # 海龟颜色

turtle.goto(189,50)
turtle.goto(182,74)
turtle.goto(174,48)
turtle.goto(189,50)
turtle.goto(174,48)
turtle.goto(157,69)
turtle.goto(182,74)
turtle.goto(174,86)
turtle.goto(157,69)
turtle.goto(142,102)
turtle.goto(174,86)
turtle.goto(189,83)
turtle.goto(190,91)
turtle.goto(174,86)
turtle.goto(190,91)
turtle.goto(190,101)
turtle.goto(174,86)
turtle.goto(169,101)
turtle.goto(190,101)
turtle.goto(174,118)
turtle.goto(169,101)
turtle.goto(142,102)
turtle.goto(174,118)
turtle.goto(156,133)
turtle.goto(142,102)
turtle.goto(134,108)
turtle.goto(156,133)

turtle.done()
'''

def Beat(n,a):
    turtle.seth(a) # 设置海龟绝对角度
    turtle.fd(n)
    turtle.seth(-a)
    turtle.fd(2*n)
    turtle.seth(a)
    turtle.fd(3*n)
    turtle.seth(-a)
    turtle.fd(4*n)
    turtle.seth(a)
    turtle.fd(3*n)
    turtle.seth(-a)
    turtle.fd(2*n)
    turtle.seth(a)
    turtle.fd(n)
    turtle.seth(0)

if __name__ == '__main__':
    turtle.setup(650, 350, 200, 200) # 设置窗口大小，和屏幕绝对位置
    turtle.penup() # 画笔抬起，海龟飞行
    turtle.fd(-280) # 海龟从原点移动
    turtle.pendown() # 画笔放下，海龟爬行
    turtle.pensize(2) # 海龟腰围
    turtle.pencolor("red") # 海龟颜色
    turtle.fd(65)

    for i in range(4):
        Beat(40, 85)
        turtle.fd(65)

    turtle.done()