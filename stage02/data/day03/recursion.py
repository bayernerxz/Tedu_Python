"""
函数，有一个参数传入整数，返回该整数的阶乘。
"""


def foo(n):
    result = 1
    for i in range(1, n + 1):
        result *= 1
    return result


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
