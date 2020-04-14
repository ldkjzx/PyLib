#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
'''
@File  : 06-1. CalStatistics.py
@Author: Jarod
@Date  : 2020/4/12 17:06
@Desc  : 

'''

def getNum():
    nums = [] # 获取用户输入的不定长数字列表
    iNumStr = input("请输入数字（回车退出）：") # 用户输入第一个数字
    while iNumStr != "": # 用户输入为空的时候停止
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字（回车退出）：") # 用户继续输入数字

    return nums


def mean(numbers): # 平均值
    s = 0.0
    for num in numbers:
        s += num
    return s/len(numbers)


def dev(numbers, mean): # 方差
    sdev = 0.0
    for num in numbers:
        sdev += (num-mean)**2
    return pow(sdev/(len(numbers)-1),0.5)


def median(numbers): # 中位数
    sorted(numbers)

    size = len(numbers)
    if size%2 == 0:
        med = (numbers[size/2-1] + numbers[size/2])/2
    else:
        med = numbers[size//2]

    return med


n = getNum()
m = mean(n)
print("平均值：{:.3f}，方差：{:.3f}，中位数：{:.3f}".format(m, dev(n,m), median(n)))
