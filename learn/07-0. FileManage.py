# -*- coding: utf-8 -*- 
"""
Project: PyLib
Author: Jarod
Create time: 2020-04-14 16:07
IDE: PyCharm
Introduction:
"""

f = open("test.txt", "wt+", encoding="utf-8")

'''
txt = f.read(2) # 每次读取两个字符，直到结束
print(txt)
txt = f.read(2)
print(txt)
txt = f.read(2)
print(txt)
txt = f.read(2)
print(txt)
txt = f.read(2)
print(txt)
'''

'''
for line in f.readlines(): # 读取全部行，返回一个列表，列表每个原始是一行
    print(line)
'''

'''
for line in f.readlines(): # 读取第一行，返回一个字符串
    print(line)
'''

'''
for line in f: # 可以直接逐行读取文件类型对象
    print(line)
'''

ls = ["中国","法国","美国"]
f.writelines(ls)
f.seek(0) # 重置指针到文件开头，否则无法打印出文件内容
for line in f:
    print(line)

f.close()