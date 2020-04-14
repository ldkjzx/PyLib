# -*- coding: utf-8 -*- 
"""
Project: PyLib
Author: Jarod
Create time: 2020-04-14 14:41
IDE: PyCharm
Introduction:
"""

def getText():
    txt = open("hamlet.txt", "r").read() # 打开文本文件
    txt = txt.lower() # 将所有字母转换成小写
    for ch in '!"#$%()*+,-./:;<>?@[\\]^_`{|}~': # 去除特殊字符，改为空格
        txt = txt.replace(ch, " ")
    return txt

hamletTxt = getText()
words = hamletTxt.split() # 通过空格分词，形成单词的列表

counts = {} # 构建空白字典，统计每个单词出现次数
for word in words:
    counts[word] = counts.get(word,0) + 1 # 如果word在字典中已存在，返回值+1；如果不存在返回0+1

items = list(counts.items()) # 将字典转换成二维列表
items.sort(key=lambda x:x[1], reverse=True) # *** 针对二维列表的第二列排序，从大到小

for i in range(100): # 取出排序后二维列表中前10组数据
    word, count = items[i] # 将每组数据拆分开
    print("{0:<10}{1:>5}".format(word, count)) # 槽位格式化，左对齐单词，右对齐数字，便于查看打印结果

