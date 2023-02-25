"""
ftp文件服务器，客户端
env:python 3.10
"""
import os, sys
import time
from socket import *

# 全局变量
SERVER_IP = "127.0.0.1"
PORT = 8888
ADDR = (SERVER_IP, PORT)
PROMPT = "\n>>>"

WELCOME = """请按需求输入下列命令：".
list 请求文件列表
get file 下载文件
put file 上传文件
quit 退出
"""
DOWNLOAD = "D:/Programming/danei/stage02 concurrent/day04/FTP_teach/Downloads/"


# 客户端文件处理类
class FTPClient:
    """
    客户端处理查看、上传、下载、退出
    """

    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        """
        获取文件库文件列表
        """
        self.sockfd.send(b"L")  # 发送请求
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == "OK":
            # 因为是TCP传输数据，会发生粘包，所以需要人为的设置消息边界
            # 一次性接收文件字符串
            data = self.sockfd.recv(4096)
            # 需要和服务端定好协议，让服务端直接以换行作为消息边界来构建消息
            print(data.decode())
        else:
            print(data)

    def download(self, file):
        self.sockfd.send(b"G " + file.encode())
        data = self.sockfd.recv(128).decode()
        if data == "OK":
            self.__recv_file(file)
        else:
            print(data)

    def __recv_file(self, file):
        """
        循环接收下载数据，并写入文件。
        :param file:需要下载的文件名
        :return:无返回值，这里仅用于跳出方法
        """
        f = open(DOWNLOAD + file, "wb")
        while True:
            data = self.sockfd.recv(1024)
            if data == b"ftp_transport_over":
                break
            f.write(data)
        f.close()

    # 自己写的
    # def upload(self, file):
    #     self.sockfd.send(b"P " + file.encode())
    #     data = self.sockfd.recv(128).decode()
    #     if data == "OK":
    #         self.__transport_file(file)
    #     else:
    #         print(data)
    #
    # def __transport_file(self, file):
    #     f = open(file, "rb")
    #     while True:
    #         data = f.read(1024)
    #         if not data:
    #             self.sockfd.send(b"ftp_transport_over")
    #             return f.close()
    #         self.sockfd.send(data)

    def upload(self, file):
        try:
            f = open(file, "rb")
        except Exception:
            print("该文件不存在")
            return
        # 获取文件名
        filename = file.split("/")[-1]
        # 发送请求
        self.sockfd.send(b"P " + filename.encode())
        data = self.sockfd.recv(128).decode()
        if data == "OK":
            self.__transport_file(f)
        else:
            print(data)

    def __transport_file(self, f):
        while True:
            data = f.read(1024)
            if not data:
                time.sleep(0.1)
                self.sockfd.send(b"ftp_transport_over")
                break
            self.sockfd.send(data)
        f.close()

    # 退出
    def quit(self):
        self.sockfd.send(b"Q")  # 请求退出
        self.sockfd.close()
        sys.exit("再见")


# 连接服务器
def main():
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print(e)
        return

    # 实例化对象，调用文件处理方法
    ftp = FTPClient(sockfd)

    # 循环发送请求
    while True:
        cmd = _hint()
        # sockfd.send(cmd.encode())  # 测试网络是否通信的代码
        _select_cmd(cmd, ftp)


def _select_cmd(cmd, ftp):
    if cmd.strip() == "list":
        ftp.do_list()
    elif cmd[:4] == "get ":
        filename = cmd[4:]
        ftp.download(filename)
    elif cmd[:4] == "put ":
        filename = cmd[4:]
        ftp.upload(filename)
    elif cmd.strip() == "quit":
        ftp.quit()
    else:
        print("请输入正确命令")


def _hint():
    print(WELCOME)
    cmd = input(PROMPT)
    return cmd


if __name__ == '__main__':
    main()
