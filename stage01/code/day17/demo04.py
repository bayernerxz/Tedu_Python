"""
    lambda 匿名函数：
        语法：lambda 参数列表: 函数体
        注意：函数体自带return
"""

from common.list_helper import *

list01 = [43, 4, 5, 5, 6, 7, 87]

# def condition01(i):
#     return i % 2 == 0
#
# def condition02(i):
#     return i > 10
#
# def condition03(i):
#     return 10 < i < 50

# for i in ListHelper.find_all(list01,condition01):
#     print(i)

for i in ListHelper.find_all(list01, lambda item: item % 2 == 0):
    print(i)

# ----------------------------------------

# 无参数函数--> lambda
def fun01():
    return 100

a = lambda: 100
re = a()

# 多参数函数--> lambda
def fun02(p1, p2):
    return p1 > p2

b = lambda p1, p2: p1 > p2
re2 = b(1, 2)
print(re2)

# 无返回值函数--> lambda
def fun03(p1):
    print("参数是：", p1)

c = lambda p1: print("参数是：", p1)
c(100)

# 方法体只能有一条语句，且不支持赋值语句
def fun04(p1):
    p1 = 2

# d = lambda p1: p1 = 2
