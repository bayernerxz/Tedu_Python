from socket import *

# 服务器地址
ADDR = ("127.0.0.1", 8888)

# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 循环收发消息
while True:
    word = input("Word>>")
    if not word:
        break
    sockfd.sendto(word.encode(), ADDR)
    msg, addr = sockfd.recvfrom(1024)
    print(word, "\t"*3, msg.decode())

sockfd.close()
