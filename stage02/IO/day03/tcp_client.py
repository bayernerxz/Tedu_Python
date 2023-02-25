"""
tcp_client.py   tcp客户端流程
重点代码
"""

from socket import *

# 创建tcp套接字
sockfd = socket()  # 使用默认参数-->tcp套接字

# 连接服务器
server_addr = ("127.0.0.1", 8888)  # 服务端地址，这里因为实在本机上演示所以用127.0.0.1，如果是真实环境，应该用0.0.0.0或这真实的服务器地址
sockfd.connect(server_addr)

while True:
    # 发送消息
    data = input("Msg>>")
    if not data:
        break
    sockfd.send(data.encode())  # 转换为字节串再发送

    # 接受消息
    data = sockfd.recv(1024)
    print("Server:", data.decode())  # 打印接受内容

# 关闭套接字
sockfd.close()
