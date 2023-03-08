"""
    列表推导式
"""

# 将list01中所有元素，增加1以后存入list02中
list01 = [1, 2, 3, 5, 6]
# list02 = []
# for item in list01:
#     list02.append(item + 1)
list02 = [item + 1 for item in list01]

# 将list01中大于4元素，增加1以后存入list02中
list02 = []
# for i in list01:
#     if i > 4:
#         list02.append(i + 1)
list02 = [i + 1 for i in list01 if i > 4]
