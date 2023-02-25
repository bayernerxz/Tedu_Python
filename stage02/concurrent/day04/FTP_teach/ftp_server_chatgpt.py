from socket import *
import os
import time

ADDR = ("0.0.0.0", 8888)
DIR = "./FTP_FILES/"


class FTPServer:
    def __init__(self):
        self.sockfd = socket()
        self.clientfd = None
        self.sockfd.bind(ADDR)
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sockfd.listen(5)

    # @staticmethod
    # def menu():
    #     """
    #     主菜单函数
    #     :return:
    #     """
    #     print("""
    #         ************************************
    #         ** Welcome to FTP server service **
    #         **             1.查看             **
    #         **             2.上传             **
    #         **             3.下载             **
    #         **             4.退出             **
    #         ************************************
    #     """)
    #
    # def run(self):
    #     while 1:
    #         print("Listen to the port 8080......")
    #         self.clientfd, addr = self.sockfd.accept()
    #         print("connect from", addr)
    #         while True:
    #             self.menu()
    #             try:
    #                 choose = int(input("请选择操作>>:"))
    #             except ValueError:
    #                 print("请输入纯数字！")
    #                 continue
    #             if choose == 1:
    #                 self.showlist()
    #             elif choose == 2:
    #                 self.upload()
    #             elif choose == 3:
    #                 self.download()
    #             elif choose == 4:
    #                 self.clientfd.close()
    #                 break
    #
    # def showlist(self):
    #     """
    #     查看文件列表
    #     :return:
    #     """
    #     file_list = os.listdir(DATABASE)
    #     if not file_list:
    #         print("该文件夹下没有文件！")
    #         return
    #     self.clientfd.send(b"OK")
    #     time.sleep(0.1)
    #
    #     # 传送文件列表
    #     data = "\n".join(file_list)
    #     self.clientfd.send(data.encode())
    #
    #     # 收命令
    #     data = self.clientfd.recv(128).decode()
    #     if data == "F":
    #         return
    #
    # def upload(self):
    #     """
    #     上传文件
    #     :return:
    #     """
    #     self.clientfd.send(b"OK")
    #     time.sleep(0.1)
    #
    #     # 接文件名
    #     file_name = self.clientfd.recv(1024).decode()
    #     time.sleep(0.1)
    #
    #     # 不允许上传文件名重复的文件
    #     file_list = os.listdir(DATABASE)
    #     if file_name in file_list:
    #         self.clientfd.send(b"NO")
    #         return
    #
    #     self.clientfd.send(b"OK")
    #     time.sleep(0.1)
    #
    #     # 收文件
    #     f = open(os.path.join(DATABASE, file_name), "wb")
    #     while True:
    #         data = self.clientfd.recv(1024)
    #         if data == b"##":
    #             break
    #         f.write(data)
    #     f.close()
    #
    # def download(self):
    #     """
    #     下载文件
    #     :return:
    #     """
    #     file_list = os.listdir(DATABASE)
    #     if not file_list:
    #         self.clientfd.send(b"NO")
    #         return
    #     self.clientfd.send(b"OK")
    #     time.sleep(0.1)
    #
    #     # 传送文件列表
    #     data = "\n".join(file_list)
    #     self.clientfd.send(data.encode())
    #     time.sleep(0.1)
    #
    #     # 接文件名
    #     file_name = self.clientfd.recv(1024).decode()
    #     time.sleep(0.1)
    #
    #     # 判断文件
    #     if file_name not in file_list:
    #         self.clientfd.send(b"NO")
    #         return
    #
    #     self.clientfd.send(b"OK")
    #     time.sleep(0.1)
    #
    #     # 发文件
    #     f = open(os.path.join(DATABASE, file_name), "rb")
    #     while True:
    #         data = f.read(1024)
    #         if not data:
    #             self.clientfd.send(b"##")
    #             break
    #         self.clientfd.send(data)
    #     f.close()

    def do_list(self, line):
        if line == 'list':
            if not os.path.exists(DIR):
                self.clientfd.send(b'OK')
                return
            else:
                file_list = os.listdir(DIR)
                if not file_list:
                    self.clientfd.send(b'OK')
                    return
                else:
                    s = "\n".join(file_list)
                    # print(len(s), s)
                    # 把bytes变成字节流, 因为传输时按字节
                    self.clientfd.send(s.encode())
                    return
        else:
            # 注册等输入其他命令
            self.clientfd.send(b'FAIL')

    def download(self):
        self.clientfd.send(b'READ')

        # 接收文件名
        filename = self.clientfd.recv(128).decode()
        print('接收到文件名：', filename)
        try:
            # 查看文件是否存在
            f = open(DIR + filename, 'rb')
        except FileExistsError:
            self.clientfd.send(b'NO')
        else:
            self.clientfd.send(b'OK')
            time.sleep(0.1)
            # 发送文件内容
            while True:
                data = f.read(4096)
                if not data:
                    break
                self.clientfd.send(data)
            f.close()
        time.sleep(0.1)
        self.clientfd.send(b'OVER')
        print('文件上传完毕')

    def do_quit(self):
        self.clientfd.send(b'EXIT')
        self.clientfd.close()

    def do_accept(self):
        self.clientfd, client_addr = self.sockfd.accept()
        print('Connect from', client_addr)

    def work(self):
        self.do_accept()
        while True:
            data = self.clientfd.recv(1024).decode()
            if not data or data == "Q":
                self.do_quit()
                return
            elif data == 'list':
                self.do_list(data)
            elif data == 'load':
                self.download()


if __name__ == '__main__':
    ftp = FTPServer()
    ftp.work()
