# 练习2：根据生日（年月日），计算活了多少天。
# 思路：
# 年月日-->出生时间
# 当前时间-->出生时间
# 计算天

import time as t


def get_life_days(year, month, day):
    birth_day = t.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
    sec = t.time() - t.mktime(birth_day)
    life_days = int(sec // (3600 * 24))
    return life_days


print(get_life_days(1983, 7, 31))
