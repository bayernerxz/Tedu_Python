"""
regex.py re模块 功能函数演示
"""

import re

# 目标字符串
s = "Alex:1994,Sunny:1996"

pattern = r"(\w+):(\d+)"  # 正则表达式

# re模块调用findall
l01 = re.findall(pattern, s)
print(l01)

# compile对象调用findall
regex = re.compile(pattern)
l02 = regex.findall(s, 0, 12)
print(l02)

# 按照正则表达式匹配内容切割字符串
l03 = re.split(r"[:,]", s)
print(l03)

# 替换目标字符串
s1 = re.sub(r":", "-", s, 1)
s2 = re.subn(r":", "-", s, 1)
print(s1, s2)
