# -*- coding: utf-8 -*- 
"""
Project: PyLib
Author: Jarod
Create time: 2020-04-15 18:24
IDE: PyCharm
Introduction:
"""

import os

libs = []
f = open("pypis.txt")
for line in f:
    line = line.replace("\n", "")
    libs.append(line)
f.close()

# libs = {"numpy", "matplotlib", "pillow", "sklearn", "requests", "jieba", "beautifulsoup4", "wheel", "networkx", "sympy", "pyinstaller", "django", "flask", "werobot", "pyqt5", "pandas", "pyopengl", "pypdf2", "docopt", "pygame"}

try:
    for lib in libs:
        os.system("pip install " + lib)
    print("Successful")
except:
    print("Failed Somehow")
