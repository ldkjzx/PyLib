# -*- coding: utf-8 -*- 
"""
Project: PyLib
Author: Jarod
Create time: 2020-04-09 16:34
IDE: PyCharm
Introduction:
"""

#weekStr = "星期一星期二星期三星期四星期五星期六星期日"
weekStr = "一二三四五六日"
weekName = "星期"
weekId = eval(input("请输入数字（1-7）："))
pos = (weekId -1)
print(weekName + weekStr[pos])

