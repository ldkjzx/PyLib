# -*- coding: utf-8 -*- 
"""
Project: PyLib
Author: Jarod
Create time: 2020-04-15 13:48
IDE: PyCharm
Introduction:
"""

import jieba
import wordcloud
import imageio

mask = imageio.imread("shape2.png")

# f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
f = open("关于实施乡村振兴战略的意见.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)

w = wordcloud.WordCloud(font_path="msyh.ttc", mask=mask, width=1000, height=700, background_color="white")
w.generate(txt)
w.to_file("grwordcloud.png")

