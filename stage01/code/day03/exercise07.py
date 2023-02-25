"""
    在控制台中获取一个整数，
    如果是偶数为变量state赋值“偶数”，否则赋值“奇数“
"""
state = "偶数" if int(input("请输入一个整数")) % 2 == 0 else "奇数"
print(state)

"""
    在控制台中录入一个年份，
    如果是闰年，给变量day赋值29，否则赋值28
"""
year = int(input("请输入年份："))
day = 29 if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else 28
print(day)
