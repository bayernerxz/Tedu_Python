# 练习：使下列代码循环执行，按e键退出。
# 调试程序

# season = input("请输入一个季度：")
#
# if season == "春":
#     print("1月2月3月")
# elif season == "夏":
#     print("4月5月6月")
# elif season == "秋":
#     print("7月8月9月")
# elif season == "冬":
#     print("10月11月12月")
# else:
#     print("输入有误！")
while True:
    season = input("请输入一个季度：")

    if season == "春":
        print("1月2月3月")
    elif season == "夏":
        print("4月5月6月")
    elif season == "秋":
        print("7月8月9月")
    elif season == "冬":
        print("10月11月12月")
    else:
        print("输入有误！")

    if input("输入e键退出") == "e":
        break
