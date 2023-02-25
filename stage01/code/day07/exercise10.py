list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# 练习1：矩阵转置，将二维列表的列，变成行
# list_result = []
# for c in range(len(list01[0])):
#     temp_list = []
#     for r in range(len(list01)):
#         temp_list.append(list01[r][c])
#     list_result.append(temp_list)
# print(list_result)

list_result = []
for c in range(len(list01[0])):
    list_result.append([])
    for r in range(len(list01)):
        list_result[c].append(list01[r][c])

print(list_result)