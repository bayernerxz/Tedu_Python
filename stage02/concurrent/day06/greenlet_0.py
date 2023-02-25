"""
协程行为示例
"""

from greenlet import greenlet


def fun1():
    print("start1")
    gr2.switch()
    print("end1")
    gr2.switch()


def fun2():
    print("start2")
    gr1.switch()
    print("end2")


# 将函数变为协程
gr1 = greenlet(fun1)
gr2 = greenlet(fun2)
gr1.switch()  # 选择执行哪个协程
