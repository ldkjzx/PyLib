# -*- coding: utf-8 -*- 
"""
Project: PyLib
Author: Jarod
Create time: 2020-04-08 16:54
IDE: PyCharm
Introduction:
"""

'''
dayfactor = 0.005
dayup = pow(1+dayfactor, 365)
daydown = pow(1-dayfactor, 365)

print("天天向上的力量{:.3f}， 天天向下的力量{:.3f}".format(dayup, daydown))
'''
def dayup(df):
    dayup = 1.0
    for i in range(365):
        if i%7 in [6,0]:
            dayup = dayup*(1-0.01)
        else:
            dayup = dayup*(1+df)
    return dayup

df = 0.01
while dayup(df) < 37.78:
    df += 0.001
print("每天努力多少：{:.3f}".format(df))

