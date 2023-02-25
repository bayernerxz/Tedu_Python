from socket import *


def file_write(file, content):
    with open("./副本 " + file.decode(), "wb") as f:
        f.write(content)


sockfd = socket()
sockfd.bind(("0.0.0.0", 8888))
sockfd.listen(5)
connfd, addr = sockfd.accept()
file_name = connfd.recv(1024)
data = connfd.recv(1024 * 1024 * 1024)
# 将data写入文件
file_write(file_name, data)
sockfd.close()
