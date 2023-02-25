"""
ftp文件服务器，服务端
env:python 3.10
多进程/线程并发 socket
"""
import os, sys
import time
from socket import *
from threading import Thread

# 全局变量
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)
FTP = "./FTP_FILES/"  # 文件库位置


# 创建类实现服务器文件处理功能
class FTPServer:
    """
    查看列表、下载、上传、退出
    """

    def __init__(self):
        self.sockfd = socket()
        self.client = None
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sockfd.bind(ADDR)
        self.sockfd.listen(5)
        print("Listening 8888")

    def view(self):
        str_filelist = ""
        for i in os.listdir("./FTP_FILES/"):
            str_filelist += i + "\n"
        self.client.send(str_filelist.encode())

    def download(self, file):
        if file not in os.listdir("./FTP_FILES/"):
            self.client.send("ftp_file_not_exist".encode())
            return
        else:
            self.client.send("ftp_ready".encode())
            f = open("./FTP_FILES/%s" % file, "rb")
            while True:
                data = f.read(1024)
                if data:
                    self.client.send("ftp_end_mark".encode())
                    return
                self.client.send(data)

    def upload(self, file):
        if file in os.listdir("./FTP_FILES/"):
            self.client.send("ftp_file_already_exist".encode())
            return
        else:
            self.client.send("ftp_ready".encode())
            f = open("./FTP_FILES/%s" % file, "wb")
            while True:
                data = self.client.recv(1024)
                if data.decode() != "ftp_end_mark":
                    f.write(data)
                else:
                    f.close()


def process_client(server):
    server.client, addr = server.sockfd.accept()
    print("Connect from ", addr)
    while True:
        instruct = server.client.recv(1024).decode()  # 接收客户端发来的指令
        # 客户端传来的指令是"L","G ABC.TXT","P ABC.TXT","Q"

        # 退出
        if not instruct or instruct == "Q":
            return print("Disconnect from ", addr)
        # 查看文件
        elif instruct == "L":
            server.view()
        # 下载文件
        elif instruct[0] == "G":
            server.download(instruct[1:])
        # 上传文件
        elif instruct[0] == "P":
            server.upload(instruct[1:])
        # 输入有误
        else:
            server.client.send("ftp_error_cmd".encode())


# 搭建网络服务端模型
def main():
    server = FTPServer()

    while True:
        th = Thread(target=process_client, args=(server,))
        th.daemon = True
        th.start()
        th.join()  # 可要可不要


if __name__ == '__main__':
    main()
