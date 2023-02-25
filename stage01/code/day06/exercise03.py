"""
    练习：在控制台中录入日期（年月），计算这是这一年的第几天。

"""
day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month = int(input("请输入月份："))
day = int(input("请输入几号："))

# 方法一
# # 前几个月的天数总和
# total_day = 0
# for i in range(month - 1):
#     total_day += day_of_month[i]
#
# total_day += day
# print(f"这一天是第{total_day}天")

# 方法二
# 前几个月的天数总和
total_day = sum(day_of_month[:month - 1]) + day
print(f"这一天是第{total_day}天")
