# 定义函数,根据年月﹐计算有多少天。考虑闰年29天，平年28天

# # 不建议方法的返回值类型可能是多种
# def calculate_day(year, month):
#     """
#     根据年月﹐计算当月有多少天
#     :param year: 年
#     :param month: 月
#     :return: 当月天数
#     """
#     if month < 1 or month > 12:
#         return 0  # 通常为了保证返回的数据是同一类型的数据，输出错误时，会返回一个不可能的值。
#     if month == 2:
#         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#             return 29
#         return 28
#     if month in (4, 6, 9, 11):
#         return 30
#     return 31

# def is_leap_year(year):
#     """
#     判定是否是闰年
#     :param year:年份
#     :return: True 是闰年 False 不是闰年
#     """
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         return True
#     return False


def is_leap_year(year):
    """
    判定是否是闰年
    :param year:年份
    :return: True 是闰年 False 不是闰年
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# def calculate_day(year, month):
#     """
#     根据年月﹐计算当月有多少天
#     :param year: 年
#     :param month: 月
#     :return: 当月天数
#     """
#     if month < 1 or month > 12:
#         return 0  # 通常为了保证返回的数据是同一类型的数据，输出错误时，会返回一个不可能的值。
#     if month == 2:
#         if is_leap_year(year):
#             return 29
#         return 28
#     if month in (4, 6, 9, 11):
#         return 30
#     return 31


def calculate_day(year, month):
    """
    根据年月﹐计算当月有多少天
    :param year: 年
    :param month: 月
    :return: 当月天数
    """
    if month < 1 or month > 12:
        return 0  # 通常为了保证返回的数据是同一类型的数据，输出错误时，会返回一个不可能的值。
    if month == 2:
        return 29 if is_leap_year(year) else 28  # 返回值的if else语法
    if month in (4, 6, 9, 11):
        return 30
    return 31
