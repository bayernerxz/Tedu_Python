"""
    练习1：定义函数，根据年月日，返回星期数。
    “星期一”，“星期二”，“星期三”，...
    思路：年月日-->时间元组
        时间元组-->星期
        星期-->格式
"""
import time as t


def get_weekday(year, month, day):
    """
    获取星期数
    :param year: 年，int类型
    :param month: 月，int类型
    :param day: 日，int类型
    :return: 星期数，str类型
    """
    str_time = f"{year}年{month}月{day}日"
    tuple_time = t.strptime(str_time, "%Y年%m月%d日")
    tuple_weekday = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期天")
    return tuple_weekday[tuple_time.tm_wday]


if __name__ == "__main__":
    print(get_weekday(2022, 12, 10))
