"""
进程对象属性
"""

from multiprocessing import Process, freeze_support
import time


def tm():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)


if __name__ == "__main__":
    freeze_support()
    p = Process(target=tm, name="新的名称")
    print("is alive:", p.is_alive())  # False
    p.daemon = True  # 父进程退出子进程也退出
    p.start()
    time.sleep(1)
    print("Name:", p.name)  # 进程名称，默认是Process-1,2,3...
    print("PID:", p.pid)  # 对应子进程PID
    print("is alive:", p.is_alive())  # True，是否在生命周期
