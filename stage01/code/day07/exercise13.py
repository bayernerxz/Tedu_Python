# 练习：定义在控制台中打印一维列表的函数
# 例如：[1,2,3]--> 1 2 3 每个元素一行

def print_list_element(ref_list):
    """
    打印列表元素，每个元素一行
    :param ref_list: 目标列表
    """
    for item in ref_list:
        print(item)


print_list_element([1, 2, 3])
