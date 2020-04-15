# -*- coding: utf-8 -*- 
"""
Project: PyLib
Author: Jarod
Create time: 2020-04-15 14:58
IDE: PyCharm
Introduction:
"""

import random

def printInfo(): # 打印提示信息
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")

def getInputs(): # 输入选手能力值和比赛场数
    a = eval(input("请输入选手A的能力值（0.00-1.00）："))
    b = eval(input("请输入选手B的能力值（0.00-1.00）："))
    n = eval(input("模拟比赛的场次："))
    return a, b, n

def gameOver(scoreA, scoreB): # 通过A和B的得分，判断比赛是否结束
    return scoreA==15 or scoreB==15


def simOneGame(probA, probB): # A和B比赛一场，分别得分数
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB): # 如果比赛还未结束，进行下一次较量
        if serving == "A": # 如果A发球，随机能力值在A的范围内，A获胜加一分；否则交换发球权
            if random.random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:               # 如果B发球，随机能力值在B的范围内，B获胜加一分；否则交换发球权
            if random.random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB


def simNGames(n, probA, probB): # A和B n场比赛一共的胜负数统计
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB) # n场比赛，每场调用单次比赛方法，返回单次比赛得分情况
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def printSummary(winsA, winsB): # 打印结果
    n = winsA +winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:.1%}".format(winsA, winsA/n))
    print("选手B获胜{}场比赛，占比{:.1%}".format(winsB, winsB/n))


def main():
    printInfo()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


if __name__ == '__main__':
    main()
