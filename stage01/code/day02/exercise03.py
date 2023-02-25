"""
古代的秤一斤是16两
练习：在控制台中获取两，计算是几斤零几两
"""

liang = int(input("请输入共几辆"))
jin = liang // 16
yuliang = liang % 16

print("结果是" + str(jin) + "斤零" + str(yuliang) + "两。")
