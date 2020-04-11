#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
'''
@File  : 05-2. HanoTower.py
@Author: Jarod
@Date  : 2020/4/11 16:04
@Desc  : 

'''

'''
def f(n):
    if n==1 or n==2:
        return 1
    else:
        return f(n-1)+f(n-2)

for i in range(1,101):
    print(f(i), end=",")
'''

count=0
def hanoi(n, src, dst, mid):
    global count
    if n == 1: # 如果只有一个圆盘，直接将圆盘从A搬到B即可
        print("{}:{}->{}".format(1,src,dst))
        count += 1
    else: # 如果超过一个圆盘，则需要通过中间柱子过渡一下
        hanoi(n-1, src, mid, dst) # 先把除了最后一个之外的所有上面的圆盘，搬到中间柱子暂存
        print("{}:{}->{}".format(n,src,dst)) # 最后一个圆盘，搬到目的地
        count += 1
        hanoi(n-1, mid, dst, src) # 把除了最后一个之外的所有上面圆盘，从中间柱子搬到目的地

hanoi(5, "A", "C", "B")
print(count)
