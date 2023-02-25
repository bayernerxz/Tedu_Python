"""
计算一个字符串中的字符以及出现的次数
# 思想：
# 逐一判断字符出现的次数。
# 如果统计过则增加1，如果没统计过则等于1.
abcdefce
a 1
b 1
c 2
d 1
e 2
f 1
"""
string = "abcdefce"
dict_letter_statistics = {}

for letter in string:
    if letter not in dict_letter_statistics:
        dict_letter_statistics[letter] = 1
    else:
        dict_letter_statistics[letter] += 1

for k, v in dict_letter_statistics.items():
    print("%s %d" % (k, v))
