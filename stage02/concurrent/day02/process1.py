"""
multiprocessing 模块创建过程
1.编写进程函数
2.生成进度对象
3.启动进程
4.回收进程
"""

import multiprocessing as mp
from time import sleep

a = 1


def fun():
    print('这是一个新进程')
    sleep(2)
    global a
    print("a=", a)
    a=10000
    print("子进程结束")


if __name__ == '__main__':
    mp.freeze_support()
    p = mp.Process(target=fun)
    p.start()

    # 父进程事件，需要在start和join之间写父进程同时做的事情。
    sleep(3)
    print("父进程干点事")

    p.join()  # 回收进程
    print("a=", a)

"""上面的3几句等同于下面的代码
    pid=os.fork()
    if pid==0:
        fun()
        os._exit()
    else:
        os.wait()
"""
