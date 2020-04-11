#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
'''
@File  : 05-1. 7pipline.py
@Author: Jarod
@Date  : 2020/4/11 10:38
@Desc  : 

'''

import turtle, time

def drawGap(): # 绘制线段头尾的空缺
    turtle.penup()
    turtle.fd(5)

def drawline(draw): # 绘制数码管
    drawGap() # 线段首空缺
    turtle.pendown() if draw else turtle.penup() #根据draw值判断画笔抬起还是落下
    turtle.fd(40)
    drawGap() # 线段尾空缺
    turtle.right(90)

def drawDigit(digit): # 绘制数字
    # 下半部分
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False) # 绘制第一条线
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False) # 绘制第二条线
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False) # 绘制第三条线
    drawline(True) if digit in [0,2,6,8] else drawline(False) # 绘制第四条线
    turtle.left(90)
    # 上半部分
    drawline(True) if digit in [0, 4, 5, 6, 8, 9] else drawline(False)  # 绘制第五条线
    drawline(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawline(False)  # 绘制第六条线
    drawline(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawline(False)  # 绘制第七条线
    # 转移到第二个数字绘制起点
    turtle.left(180)
    turtle.penup()
    turtle.fd(20) # 间隔20像素

def drawDate(date): # 绘制输出数字，datew为日期，格式为 “%Y-%m=%d+”
    for i in date:
        if i == '-':
            turtle.write('年', font=("Arial", 18, "normal")) # 写文字
            turtle.color("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月', font=("Arial", 18, "normal"))  # 写文字
            turtle.color("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日', font=("Arial", 18, "normal"))  # 写文字
        else:
            drawDigit(eval(i))

def main(): # 主函数，程序运行起点
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-330)
    turtle.pensize(5)
    turtle.pencolor("red")
    drawDate(time.strftime('%Y-%m=%d+', time.gmtime()))
    turtle.hideturtle()
    turtle.done()

if __name__ == '__main__':
    main()


