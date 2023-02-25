"""
测试用例
"""
import time
# from multiprocessing import Process, freeze_support
# from threading import Thread


def decorator(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print("耗时%.2fs" % (t2 - t1))

    return wrapper


# 计算
@decorator
def count(x, y, c):
    while c < 7000000:
        x += 1
        y += 1
        c += 1


def io():
    write(180000)
    read()


def write(count_):
    f = open("test.JPG", "w", encoding="utf-8")
    for i in range(count_):
        f.write("Hello world\n")
    f.close()


def read():
    f = open("test.JPG")
    f.readlines()
    f.close()


if __name__ == "__main__":
    # count(0, 0, 0)  # 单进程耗时0.44

    # freeze_support()
    # t1 = time.time()
    # jobs = []
    # for i in range(10):
    #     p = Process(target=count, args=(0, 0, 630000))
    #     jobs.append(p)
    #     p.start()
    # for i in jobs:
    #     i.join()
    # t2 = time.time()
    # print("耗时%.2fs" % (t2 - t1))  # 10进程耗时1.00以上

    # freeze_support()
    # t1 = time.time()
    # jobs = []
    # for i in range(10):
    #     t = Thread(target=count, args=(0, 0, 630000))
    #     jobs.append(t)
    #     t.start()
    # for i in jobs:
    #     i.join()
    # t2 = time.time()
    # print("耗时%.2fs" % (t2 - t1))  # 10线程耗时4.00以上

    # io()  # 单进程耗时0.93s

    # t1 = time.time()
    # jobs = []
    # for i in range(10):
    #     p = Process(target=io)
    #     jobs.append(p)
    #     p.start()
    # for i in jobs:
    #     i.join()
    # t2 = time.time()
    # print("耗时%.2fs" % (t2 - t1))  # 10进程耗时0.4s左右

    # t1 = time.time()
    # jobs = []
    # for i in range(10):
    #     t = Thread(target=io)
    #     jobs.append(t)
    #     t.start()
    # for i in jobs:
    #     i.join()
    # t2 = time.time()
    # print("耗时%.2fs" % (t2 - t1))  # 10线程耗时0.66s左右

    pass
