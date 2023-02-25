from time import sleep
import os
import sys


def f1():
    for i in range(3):
        sleep(2)
        print("write")


def f2():
    for i in range(2):
        sleep(4)
        print("test")


pid = os.fork()
if pid < 0:
    print("error")
elif pid == 0:  # 一级子进程
    p = os.fork()
    if p < 0:
        print("error")
    elif p == 0:  # 二级子进程
        f1()
    else:  # 一级子进程
        os._exit(0)
else:  # 父进程
    os.wait()  # 等一级子进程
    f2()
