# -*- coding: utf-8 -*- 
"""
Project: PyLib
Author: Jarod
Create time: 2020-04-14 16:28
IDE: PyCharm
Introduction:
"""

import turtle as t

t.title("自动轨迹绘制")
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)

details = []
f = open("data.txt")
for line in f:
    line = line.replace("\n","") # 去除每行最后的换行符
    details.append(list(map(eval, line.split(",")))) # 将每行数据变成一个列表，存在二维表details中
f.close()

for i in range(len(details)):
    t.pencolor(details[i][3], details[i][4], details[i][5])
    t.fd(details[i][0])
    if details[i][1]:
        t.right(details[i][2])
    else:
        t.left(details[i][2])

