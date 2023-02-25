"""
计算列表中的最小值（不使用min()函数）
"""

list01 = [54, 25, 13, 23, 43, 35, 17]
min_num = list01[0]
for i in list01:
    if i < min_num:
        min_num = i
print(f"最小的数是{min_num}")
