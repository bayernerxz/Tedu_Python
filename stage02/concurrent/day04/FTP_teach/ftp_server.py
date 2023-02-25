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
FTP = "D:/Programming/danei/stage02 concurrent/day04/FTP_teach/FTP_FILES/"  # 文件库位置


# 创建类实现服务器文件处理功能
class FTPServer(Thread):
    """
    查看列表、下载、上传、退出
    """

    def __init__(self, connfd, addr):
        super().__init__()
        # 连接的客户端套接字
        self.connfd = connfd
        self.addr = addr

    # 循环接收请求，分情况调用功能函数
    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            # print(data)  # 网络连接测试代码

            if not data or data == "Q":  # 如果Ctrl+C退出客户端，data返回的是空。
                return print("Disconnect from", self.addr)  # 这里使用return直接表示线程线束
            elif data == "L":
                self.do_list()
            elif data[0] == "G":
                self.download(data[2:])  # 文件名需要从第三个字符开始取
            elif data[0] == "P":
                self.upload(data[2:])  # 文件名需要从第三个字符开始取

    # 实现发送文件列表
    def do_list(self):
        # 获取文件列表
        files = os.listdir(FTP)
        if not files:
            self.connfd.send("文件库为空")
            return
        self.connfd.send(b"OK")
        time.sleep(0.1)  # 防止与后面发送的文件名发生粘包
        self.__send_file_list(files)

    def __send_file_list(self, files):
        # 使用换行符拼接文件
        filelist = ""
        for file in files:
            if file[0] != "." and os.path.isfile(FTP + file):  # 在Linux下判断是否是隐藏文件
                filelist += file + "\n"
        self.connfd.send(filelist.encode())

    # 实现文件下载
    def download(self, file):
        try:
            f = open(FTP + file, "rb")
        except FileExistsError:
            # 打开失败文件不存在
            self.connfd.send("文件不存在\n".encode())
            return
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1)  # 防止粘包
        self.__transport_file(f)

    def __transport_file(self, f):
        # 发送文件
        while True:
            data = f.read(1024)
            if not data:
                time.sleep(0.1)  # 防止粘包
                return self.connfd.send(b"ftp_transport_over")
            self.connfd.send(data)

    # 实现文件上传
    def upload(self, file):
        if file in os.listdir(FTP):  # os.path.exists(FTP+file)可实现同样的功能
            return self.connfd.send("文件已存在".encode())
        else:
            self.connfd.send(b"OK")
        self.__recv_file(file)

    def __recv_file(self, file):
        """
        接收文件
        :param file: 文件名
        :return:
        """
        f = open(FTP + file, "wb")
        while True:
            data = self.connfd.recv(1024)
            if data == b"ftp_transport_over":
                break
            f.write(data)
        f.close()


# 搭建网络服务端模型
def main():
    s = _create_socket()
    print("Listen the port 8888")
    _handle_client_link(s)


def _create_socket():
    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 设置套接字的端口重用
    s.bind(ADDR)
    s.listen(5)
    return s


def _handle_client_link(s):
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
        _create_client_socket(c, addr)


def _create_client_socket(c, addr):
    # 创建线程处理请求
    client = FTPServer(c, addr)
    client.daemon = True
    client.start()  # 运行run


if __name__ == '__main__':
    main()
