"""
粘包演示
"""

from socket import *
from time import sleep

sockfd = socket()
sockfd.bind(("127.0.0.1", 8888))
sockfd.listen(5)
connfd, addr = sockfd.accept()

while True:
    sleep(1)
    data = connfd.recv(1024)
    print(data.decode())
