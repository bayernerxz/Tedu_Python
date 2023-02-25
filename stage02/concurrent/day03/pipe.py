"""
pipe.py 管道通信
注意:
    1. multiprocessing 中管道通信只能用于有亲缘关系进程中
    2.管道对象在父进程中创建，子进程通过父进程获取
"""
from multiprocessing import Process, Pipe, freeze_support

# 创建管道
fd1, fd2 = Pipe()


# fd1, fd2 = Pipe(False)  # 如果是单向管道，fd1->recv，fd2->send


def app1(fd1):  # 在windows使用管道间通信方法，需要传参。
    print("启动app1,请登录")
    print("请求app2授权")
    fd1.send("app1请求登录")  # 写入管道
    data = fd1.recv()
    if data:
        print("登录成功：", data)


def app2(fd2):
    data = fd2.recv()  # 阻塞等待读取管道内容
    print(data)
    fd2.send(("Dave", "123"))  # 可以发送任意Python类型数据


if __name__ == "__main__":
    freeze_support()
    p1 = Process(target=app1, args=(fd1,))
    p2 = Process(target=app2, args=(fd2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
