"""
进程池使用示例
"""

from multiprocessing import Pool, freeze_support
from time import sleep, ctime


# 进程池事件
def worker(message):
    sleep(2)
    print(ctime(), "--", message, "\n")


if __name__ == "__main__":
    freeze_support()

    # 创建进程池
    pool = Pool()

    # 向进程池队列添加事件
    for i in range(10):
        msg = "TDU %d" % i
        pool.apply_async(func=worker, args=(msg,))

    # 关闭进程池
    pool.close()

    # 回收进程池
    pool.join()
