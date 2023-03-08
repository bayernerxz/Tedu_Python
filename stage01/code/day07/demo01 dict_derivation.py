"""
    字典推导式
"""

# 1，2，3，4……10 -> 平方
dict01 = {}
for item in range(1, 11):
    dict01[item] = item ** 2
print(dict01)

# 推导式：
dict02 = {item: item ** 2 for item in range(1, 11)}
print(dict02)

# 只大于5的数字
dict03 = {}
for item in range(1, 11):
    if item > 5:
        dict03[item] = item ** 2
print(dict03)

dict04 = {item: item ** 2 for item in range(1, 11) if item > 5}
print(dict04)
