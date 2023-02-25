"""
    练习1：在控制台中，获取一个开始值，一个结束值。
        将中间的数字打印出来。
"""

start = int(input("请输入一个起始值"))
end = int(input("请输入一个结束值"))

while start < end - 1:
    start += 1
    print(start)
