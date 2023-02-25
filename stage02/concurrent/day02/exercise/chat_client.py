"""
chat room 客户端
发送请求，展示结果
"""
from socket import *
import os, sys

# 服务器地址
ADDR = ("127.0.0.1", 8888)


# 进入聊天室
def enter_room(socket_):
    while True:
        user_name = input("请输入用户名：")
        msg = "L " + user_name
        socket_.sendto(msg.encode(), ADDR)
        # 接收反馈
        data = socket_.recvfrom(128)[0].decode()
        if data == "OK":
            print("%s,您已经进入聊天室。" % user_name)
            return user_name
        else:
            print(data)


# 发送消息
def send_msg(s, name):
    while True:
        try:
            text = input(">>")
        except KeyboardInterrupt:
            text = "quit"
        if text.strip() == "quit":
            msg = "Q " + name
            s.sendto(msg.encode(), ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s" % (name, text)
        print(name, ":", text)
        s.sendto(msg.encode(), ADDR)


# 接收消息
def recv_msg(s):
    while True:
        try:
            data, addr = s.recvfrom(4096)
        except KeyboardInterrupt:
            sys.exit()
        # 从服务器收到EXIT退出
        if data.decode() == "EXIT":
            sys.exit()
        print(data.decode() + "\n>>", end="")


# 客户端启动函数
def main():
    s = socket(AF_INET, SOCK_DGRAM)
    name = enter_room(s)

    # 已经进入聊天室
    pid = os.fork()
    if pid < 0:
        sys.exit("error")
    elif pid == 0:
        send_msg(s, name)  # 子进程负责消息发送
    else:
        recv_msg(s)  # 父进程负责消息接收


main()
