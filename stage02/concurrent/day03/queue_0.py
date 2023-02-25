"""
queue_0.py 消息队列演示
注意：消息队列符合先进先出原则
"""
from multiprocessing import Queue, Process, freeze_support
from time import sleep
from random import randint


def handle(q):  # 在windows下IPC需要传参
    for i in range(6):
        x = randint(1, 33)
        q.put(x, block=False)  # 消息入队
    x = randint(1, 16)
    q.put(x, block=False)


def request(q):
    list01 = []
    for i in range(6):
        list01.append(q.get())
    list01.sort()
    list01.append(q.get())
    print(list01)


if __name__ == "__main__":
    freeze_support()
    # 创建消息队列
    q = Queue(8)
    p1 = Process(target=handle, args=(q,))
    p2 = Process(target=request, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
