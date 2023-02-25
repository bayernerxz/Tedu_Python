# 练习3：再控制台中分别录入4个数字
# 打印最大的数字

num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))
num3 = float(input("请输入第三个数字："))
num4 = float(input("请输入第四个数字："))

temp = num1

if temp < num2:
    temp = num2
if temp < num3:
    temp = num3
if temp < num4:
    temp = num4

print("最大的数字是"+str(temp))
