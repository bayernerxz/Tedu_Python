# 练习：在控制台中获取月份，显示季度，或者提示月份错误

month = int(input("请输入月份数："))
if month > 12 or month < 1:
    print("输入错误！")
elif month in [1, 2, 3]:
    print("一季度")
elif month in [4, 5, 6]:
    print("二季度")
elif month in [7, 8, 9]:
    print("三季度")
else:
    print("四季度")
