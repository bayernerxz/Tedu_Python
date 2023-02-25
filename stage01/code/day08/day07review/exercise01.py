# 3．定义在控制台中打印二维列表的函数
# [
# 	[1,2,3,44],
# 	[4,5,5,5,65,6,87],
# 	[ 7,5]
# ]
#
# 1 2 3 44
# 4 5 5 5 65 6 87
# 7 5

def print_double_list(ref_matrix):
    """
    打印二维列表
    :param ref_matrix: 目标二维数组
    """
    for item in ref_matrix:
        for item2 in item:
            print(item2, end=" ")
        print()


list01 = [
    [1, 2, 3, 44],
    [4, 5, 5, 5, 65, 6, 87],
    [7, 5]
]
print_double_list(list01)
