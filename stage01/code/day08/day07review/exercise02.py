# 4．(扩展)方阵转置。(不用做成函数)
# 提示∶详见图片
# （因为是方阵，可以把每个大方阵的最外面交换。然后方阵边长减少1，再作一次。直到方阵边长为2。）

def transpose_array(ref_list):
    """
    转置方阵
    :param ref_list:目标列表
    """
    for j in range(1, len(ref_list)):
        for i in range(j, len(ref_list)):
            list01[j - 1][i], list01[i][j - 1] = list01[i][j - 1], list01[j - 1][i]
    return ref_list


list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(transpose_array(list01))
# [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]
