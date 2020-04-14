#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
'''
@File  : 05-3. KochDraw.py
@Author: Jarod
@Date  : 2020/4/12 11:00
@Desc  : 

'''

import turtle

def koch(size, n):
    if n==0: # 0阶曲线直接画直线
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]: # 四次转角，画四个线段，组成一个雪花边
            turtle.left(angle)
            koch(size/3, n-1)

def main():
    turtle.setup(800, 800)
    turtle.penup()
    turtle.goto(-300, -150)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor("blue")

    turtle.left(60)
    for i in range(3):
        koch(600, 3)
        turtle.right(120)
    turtle.hideturtle()
    # turtle.done()

if __name__ == '__main__':
    main()

