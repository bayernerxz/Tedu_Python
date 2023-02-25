"""
4．定义函数﹐计算指定范围内的素数
"""


def get_prime_number(end=2, begin=0):
    """
    指定范围内的素数
    :param end:范围终止的数字，不含。
    :param begin: 范围起始的数字
    :return: 该范围内素数的列表
    """
    list_result = [2]
    if end <= 3:
        return list_result
    for i in range(3, end):
        for item in list_result:
            if i % item == 0:
                break
        else:
            list_result.append(i)

    return [i for i in list_result if i >= begin]


print(get_prime_number(5))


# def get_prime(begin, end):
#     list_result = []
#     # 生成范围内的整数
#     for i in range(begin, end):
#         # 判断素数
#         for item in range(2, i):
#             if i % item == 0:
#                 break
#         else:
#             list_result.append(i)
#     return list_result


def is_prime(number):
    """
    判断指定的数字是否为素数
    :param number: 指定的素数
    :return: True表示是素数，False不是
    """
    for item in range(2, number):
        if number % item == 0:
            break
    return True


def get_prime(begin, end):
    """
    获取范围内的素数
    :param begin:开始值（包含）
    :param end: 结束值（不包含）
    :return:
    """
    return [i for i in range(begin, end) if is_prime(i)]


print(get_prime(25, 3))
