# 练习2：使用客户端查询单词，得到单词的解释，
# 如果没有该单词则得到“没有单词”。客户端可以循环输入单词，
# 直到输入空退出。

# 服务端提供逻辑和数据处理
from socket import *


def find_word(word):
    f = open("dict2.txt", encoding="utf-8")
    for line in f:
        w = line.split(" ")[0]
        # 如果遍历到的单词已经大于word就结束查找
        if w > word:
            f.close()
            return "没有找到该单词"
        elif w == word:
            f.close()
            return line
    else:
        f.close()
        return "没有找到该单词"


# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
server_addr = ("0.0.0.0", 8888)
sockfd.bind(server_addr)

# 收发消息
while True:
    try:
        data, addr = sockfd.recvfrom(1024)
        # 查单词
        result = find_word(data.decode())
        sockfd.sendto("单词解释", addr)
    except KeyboardInterrupt:
        break

# 关闭套接字
sockfd.close()
