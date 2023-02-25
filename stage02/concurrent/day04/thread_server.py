"""
thread_server.py 基于threading多线程并发
重点代码

1. 创建监听套接字
2. 等待接收客户端请求
3. 当有新的客户端连接，创建线程处理客户端请求
4. 主线程继续等待其他客户端连接
5. 如果客户端退出，则对应分支线程退出
"""

from socket import *
from threading import Thread
import sys


# 具体处理客户端请求
def handle(connfd_):
    while True:
        data = connfd_.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd_.send(b"OK")
    connfd_.close()


# 设置全局变量
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 1.创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 设置套接字的端口重用
s.bind(ADDR)
s.listen(5)

print("Listen the port 8888")

while True:
    # 循环处理客户端连接
    try:
        c, addr = s.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        sys.exit("退出服务器")
    except Exception as e:
        print(e)
        continue

    # 创建线程处理请求
    t = Thread(target=handle, args=(c,))
    t.daemon = True
    t.start()
