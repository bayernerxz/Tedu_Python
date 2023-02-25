"""
block_io.py
socket 套接字非阻塞示例
"""
from socket import *
from time import ctime, sleep

# 日志文件
f = open("log.txt", "a+")

# tcp套接字
s = socket()
s.bind(("0.0.0.0", 8888))
s.listen(3)

# 设置套接字为非阻塞
# s.setblocking(False)

# 设置超时检测
s.settimeout(3)

while True:
    print("Waiting for connect...")
    # 没有客户端连接，每隔3秒写一条日志
    try:
        connfd, addr = s.accept()
    except (BlockingIOError, timeout) as e:  # 同时捕获多个异常的时候需要使用元组封装
        sleep(3)
        f.write("%s：%s" % (ctime(), e))
        f.flush()
    else:
        print("Connecting from", addr)
        data = connfd.recv(1024).decode()
        print(data)
