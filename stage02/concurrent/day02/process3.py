"""
Process 给进程函数传参
"""

from multiprocessing import Process, freeze_support
from time import sleep


# 带参数的进程函数
def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm %s" % name)
        print("I'm working...")


if __name__ == '__main__':
    freeze_support()
    # p = Process(target=worker, args=(2, "Baron"))
    p = Process(target=worker, args=(2,), kwargs={"name": "Baron"})  # 作用同上
    p.start()
    p.join()
