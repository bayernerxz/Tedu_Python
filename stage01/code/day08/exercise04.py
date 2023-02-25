# 练习：定义 判断列表中是否存在相同元素的函数

def judge_same_element(ref_list):
    """
    判断列表中是否存在相同元素
    :return: True or False
    """
    for i in range(len(ref_list) - 1):
        for j in range(i + 1, len(ref_list)):
            if ref_list[i] == ref_list[j]:
                return True
    return False


print(judge_same_element([3, 80, 45, 5, 80, 1]))
