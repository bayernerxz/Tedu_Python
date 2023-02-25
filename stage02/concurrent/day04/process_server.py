"""
process_server.py 基于fork的多进程开发
重点代码

1. 创建监听套接字
2. 等待接收客户端请求
3. 客户端连接创建新的进程处理客户端请求
4. 原进程继续等待其他客户端连接
5. 如果客户端退出，则销毁对应的进程
"""

from socket import *
import os, signal
from multiprocessing import Process, freeze_support


# 具体处理客户端请求
def handle(connfd_):
    while True:
        data = connfd_.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd_.send(b"OK")
    connfd_.close()


if __name__ == "__main__":
    freeze_support()
    # 全局变量
    HOST = "0.0.0.0"
    PORT = 8888
    ADDR = (HOST, PORT)

    # 1.创建监听套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 设置套接字的端口重用
    s.bind(ADDR)
    s.listen(5)
    print("Listen the port 8888")

    # # 处理僵尸进程(因为fork只在linux下，所以下面这个single语句中的两个SIGCHLD和SIG_IGN在WINDOWS中的python版本中不存在)
    # signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    while True:
        # 循环处理客户端连接
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            os._exit(0)
        except Exception as e:
            print(e)
            continue

        p = Process(target=handle, args=(c,))
        p.daemon = True  # 父进程结束则所有服务终止
        p.start()
