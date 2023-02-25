# 在控制台中获取一个整数，判断是否为素数。
input_number = int(input("请输入一个整数："))
if input_number <= 1:
    print("不是素数")
for item in range(2, input_number):
    if input_number % item == 0:
        print("不是素数")
        break
else:
    print("是素数")
