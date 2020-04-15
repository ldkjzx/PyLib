# -*- coding: utf-8 -*- 
"""
Project: PyLib
Author: Jarod
Create time: 2020-04-15 12:02
IDE: PyCharm
Introduction:
"""

import jieba
import wordcloud

'''
txt = "life is short, you need python"
w = wordcloud.WordCloud(background_color="white")
w.generate(txt)
w.to_file("pywordcloud.png")
'''
txt = "程序设计语言是计算机能顾理解和识别用户操作意图的一种交互体系，它按照特定规则组织计算机指令，是计算机能够自动运行各种运算处理。"
w = wordcloud.WordCloud(width=1000, height=700, font_path="msyh.ttc")

w.generate(" ".join(jieba.lcut(txt)))
w.to_file("pywordcloud.png")