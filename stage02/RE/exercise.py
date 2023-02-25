"""
1．匹配一个.com邮箱格式字符串
2．匹配一个密码8-12位数字字母下划线构成
3．匹配一个数字正数，负数﹐整数﹐小数﹐分数1/2﹐百分数45%
4．匹配一段文字中以大写字母开头的单词﹐注意文字中可能有iPython(不算)H-base(算)
单词可能有 大写字母 小写字母 - _
"""

import re

# 1．匹配一个.com邮箱格式字符串
s = "zhaoqian:doif@qq.com"
print(re.findall(r"\w*@\w+\.com", s))

# 2．匹配一个密码8-12位数字字母下划线构成
s = "password:123_abcA"
print(re.findall(r"\w{8,12}", s))

# 3．匹配一个数字正数，负数﹐整数﹐小数﹐分数1/2﹐百分数45%
s = "25, -45, 2.3, -0.34, 0, 1/2, 45%"
print(re.findall(r"-?\d+/?\.?\d*%?", s))

# 4．匹配一段文字中以大写字母开头的单词﹐注意文字中可能有iPython(不算)H-base(算)
# 单词可能有 大写字母 小写字母 - _

s = """Project description

(The development of this package has not finished.)

hbase-python is a python package used to work HBase.

It is now tested under H-Base 1.2.6.

Before using HBase, we are familiar with Mongo-DB and pymongo. 

While, when coming to HBase, we found it is not easy to access the database via iPython. 

So, I spent some days to start this project and hope it can be helpful to our daily research work. 

The thought of this package comes from “happybase” and “starbase”, and I am trying to make the API behaves like “pymongo”.
"""

print(re.findall(r"\b[A-Z][_\-A-Za-z]*\b", s))
