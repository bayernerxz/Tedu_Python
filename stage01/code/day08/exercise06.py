# 定义列表升序排列的函数

def sort_list_ascending(ref_list):
    """
    升序排列列表
    :param ref_list: 需要排列的列表
    :return: 返回排列完成的列表
    """
    # 满足以下两个条件，就无需通过返回值传递结果。
    # 1、传入的是可变对象
    # 2、函数体修改传入的对象
    for i in range(len(ref_list) - 1):
        for j in range(i + 1, len(ref_list)):
            if ref_list[i] > ref_list[j]:
                ref_list[i], ref_list[j] = ref_list[j], ref_list[i]


list01 = [3, 2, 1]
sort_list_ascending(list01)
print(list01)
