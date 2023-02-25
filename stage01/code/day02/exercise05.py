"""
练习：
在控制台中录入一个四位整数：1234
计算每位相加和。1+2+3+4
显示结果。
"""

number = int(input("请输入一个四位整数："))

# ones = number % 10
# number -= ones
# tens = number % 100 / 10
# number -= tens * 10
# hundreds = number % 1000 / 100
# number -= hundreds * 100
# thousands = number / 1000

# 方法一
# ones = number % 10
# tens = number // 10 % 10
# hundreds = number // 100 % 10
# thousands = number // 1000
#
# result = ones + tens + hundreds + thousands

# 方法二
result = number % 10
result += number // 10 % 10
result += number // 100 % 10
result += number // 1000

print("结果是：" + str(result))
