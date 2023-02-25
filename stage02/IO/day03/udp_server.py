"""
udp_server.py UDP套接字服务端流程
重点代码
"""

from socket import *

# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
server_addr = ("127.0.0.1", 8888)
sockfd.bind(server_addr)

# 收发消息
while True:
    try:
        data, addr = sockfd.recvfrom(1024)
        print("收到消息：", data.decode())
        sockfd.sendto(b"Thanks", addr)
    except Exception:
        break

# 关闭套接字
sockfd.close()
