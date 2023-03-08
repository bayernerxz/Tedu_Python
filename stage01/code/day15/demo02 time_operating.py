"""
    时间处理
"""

import time

# 1.获取当前时间戳
# 时间戳以1970-01-01 8：00：00起始，到现在经过的秒数
print(time.time())

# 2. 时间元组(年，月，日，时，分，秒，一周的第几天，一年的第几天，夏令时)
# 时间戳 --> 时间元组
print(time.localtime(time.time()))
# 通过元组的操作获取时间
tuple_time = time.localtime()
for item in time.localtime():
    print(item)
print(tuple_time[1])  # 月

# 通过类的操作获取时间
print(type(time.localtime()))  # <class 'time.struct_time'>
print(tuple_time.tm_year)  # 年

# 时间元组 --> 时间戳
print(time.mktime(tuple_time))

#  3.时间元组 --> str
str_time = time.strftime("%Y年%m月%d日，%H时%M分%S秒", tuple_time)
print(str_time)

#  str --> 时间元组
print(time.strptime(str_time, "%Y年%m月%d日，%H时%M分%S秒"))
