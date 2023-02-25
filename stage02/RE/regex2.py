"""
regex2.py
Match对象属性演示
"""

import re

pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)

obj = regex.search("babcdefghi")  # Match对象

# 属性变量
print(obj.pos)  # 目标字符串开始搜索的位置 # 0
print(obj.endpos)  # 目标字符串结束搜索的位置 # 10
print(obj.re)  # 正则
print(obj.string)  # 目标字符串
print(obj.lastgroup)  # 最后一组组名
print(obj.lastindex)  # 最后一组序列号

print("=" * 50)
# 属性方法
print(obj.span())  # 匹配内容在字符串中位置
print(obj.start())  # 匹配内容在字符串中起始位置
print(obj.end())  # 匹配内容在字符串中结尾位置

print(obj.groupdict())  # 捕获组字典
print(obj.groups())  # 子组对应内容元组

print(obj.group())  # 获取Match对应内容 # abcdef
print(obj.group(1))  # 按子组索引获取Match对应内容 # ab
print(obj.group(2))  # ef
print(obj.group("pig"))  # 按捕获组名获取Match对应内容# ef
