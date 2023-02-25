# 练习：定义方阵转置函数

def transpose_array(ref_list):
    """
    转置方阵
    :param ref_list:二维列表类型的方阵
    """
    for j in range(1, len(ref_list)):
        for i in range(j, len(ref_list)):
            list01[j - 1][i], list01[i][j - 1] = list01[i][j - 1], list01[j - 1][i]


list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# 矩阵转置的转置等于原矩阵
transpose_array(list01)
print(list01)
transpose_array(list01)
print(list01)
