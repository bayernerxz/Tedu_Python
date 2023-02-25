# 练习2：在控制台中录入一个数字
# 再录入一个运算符（+ - * /），最后再录入一个数字
# 根据运算符，计算两个数字
# 要求：如果运算符，不是加减乘除，则提示”运算符有误“

num1 = float(input("请输入一个数字"))
operator = input("请输入一个运算符")
num2 = float(input("请再输入一个数字"))

if operator == "+":
    result = num1 + num2
    print("结果是" + str(result))
elif operator == "-":
    result = num1 - num2
    print("结果是" + str(result))
elif operator == "*":
    result = num1 * num2
    print("结果是" + str(result))
elif operator == "/":
    result = num1 / num2
    print("结果是" + str(result))
else:
    print("运算符有误")
