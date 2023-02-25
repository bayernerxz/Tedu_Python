"""
tcp_server.py tcp套接字服务端流程
重点代码

注意：
功能性代码，注重流程和函数使用
"""

import socket

# 创建tcp套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址
sockfd.bind(("127.0.0.1", 8888))

# 设置监听
sockfd.listen(5)

while True:
    # 阻塞等待处理连接
    print("Waiting for connecting...")
    try:
        connfd, addr = sockfd.accept()  # 测试可以在本地计算机终端中输入telnet 127.0.0.1 8888
        print("Connect from", addr)  # 打印连接的客户端地址
    except KeyboardInterrupt:
        print("服务器退出")
        break
    except Exception as e:
        print(e)
        continue

    n = 0  # 单次连接的发送字节串计数
    while True:
        # 收发消息
        data = connfd.recv(1024)  # 连接的客户端如果断开后，返回值为空，recv不再阻塞
        if not data:  # 如果data为空的话，说明客户端退出
            break
        print("Receive:", data.decode())
        n += connfd.send(b"Thanks")  # 发送字节串
    print("通信结束，共发送%d字节串" % n)

    # 关闭客户端套接字
    connfd.close()

# 关闭服务端套接字
sockfd.close()
