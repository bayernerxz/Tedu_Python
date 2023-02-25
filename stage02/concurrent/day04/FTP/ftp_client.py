"""
ftp文件服务器，客户端
env:python 3.10
"""
import os, sys
from socket import *

# 全局变量
SERVER_IP = "127.0.0.1"
PORT = 8888
ADDR = (SERVER_IP, PORT)
PROMPT = ">>>"

WELCOME = """请输入命令，例如\"L abc.txt\".
L 请求文件列表
Q 退出
G 下载文件
P 上传文件
"""


# 客户端文件处理类
class FTPClient:
    """
    客户端处理查看、上传、下载、退出
    """

    def __init__(self):
        self.sockfd = socket()
        self.sockfd.connect(ADDR)

    def view(self, cmd):
        self.sockfd.send(cmd.encode())
        filename = self.sockfd.recv(4096).decode()
        print(filename)

    def download(self, cmd):
        self.sockfd.send(cmd.encode())
        head = self.sockfd.recv(1024)
        if head.decode() == "ftp_file_not_exist":
            print("文件不存在。请重新输入命令。")
            return
        elif head.decode() == "ftp_ready":
            f = open("./%s" % cmd[2:], "wb")
            while True:
                data = self.sockfd.recv(1024)
                if data.decode() != "ftp_end_mark":
                    f.write(data)
                else:
                    f.close()
                    return

    def upload(self, cmd):
        self.sockfd.send(cmd.encode())
        head = self.sockfd.recv(1024)
        if head.decode() == "ftp_file_already_exist":
            print("文件已经存在。请重新输入命令。")
            return
        elif head.decode() == "ftp_ready":
            f = open("%s" % cmd[2:], "rb")
            while True:
                data = f.read(1024)
                if data:
                    self.sockfd.send("ftp_end_mark".encode())
                    return
                self.sockfd.send(data)

    def quit(self):
        self.sockfd.send(b"Q")
        sys.exit("再见")


# 连接服务器
def main():
    c = FTPClient()
    while True:
        print(WELCOME)
        instruct = input(PROMPT)
        list_instruct = instruct.split(" ")
        # 输入的指令是"L","G ABC.TXT","P ABC.TXT","Q"

        if list_instruct[0] == "L":
            c.view(instruct)
        # 下载文件
        elif list_instruct[0] == "G":
            c.download(instruct)
        # 上传文件
        elif list_instruct[0] == "P":
            c.upload(instruct)
        # 退出
        elif list_instruct[0] == "Q":
            c.quit()

        elif list_instruct[0] == "ftp_error_cmd":
            print("未知命令错误，请重新输入。")
        else:
            print("输入有误，请重新输入。")


if __name__ == '__main__':
    main()
