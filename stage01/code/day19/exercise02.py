"""
    在不改变原有功能（fun01 fun02）调用与定义情况下，
    为其增加新功能（打印函数执行时间）。
"""

import time


def timer(func):
    def wrapper(*args, **kwargs):
        init_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"执行时间是{end_time - init_time:.2f}s")
        return result

    return wrapper


@timer
def fun01():
    time.sleep(2)  # 睡眠2s，用于模拟程序执行的过程
    print("fun01执行完毕喽")


@timer
def fun02(a):
    time.sleep(2)
    print("fun02执行完毕喽，参数是", a)


fun01()
fun02(100)
