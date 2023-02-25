# 再控制台中获取一个月份
# 打印天数：或者提示输入有误

month = int(input("请输入月份数："))

if month == 2:
    print("有28天")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print("有31天")
elif month in [4, 6, 9, 11]:
    print("有30天")
else:
    print("输入有误")
