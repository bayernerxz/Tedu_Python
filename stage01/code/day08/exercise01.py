"""
    练习：定义计算四位整数，每位相加和的函数。
    测试：“1234”等
"""


def add_each_unit(ref_num):
    """
    计算整数的每位相加和
    :param ref_num: 四位整数
    :return: 相加的结果
    """
    result = ref_num % 10
    # 累加十位
    result += ref_num // 10 % 10
    # 累加百位
    result += ref_num // 100 % 10
    # 累加千位
    result += ref_num // 1000
    return result


# 测试时，越简洁越好
print(add_each_unit(1234))
print(add_each_unit(5678))
