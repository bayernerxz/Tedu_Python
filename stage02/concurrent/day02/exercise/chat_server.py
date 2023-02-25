"""
chat room
env:python3.10
socket udp & fork
"""

from socket import *
import os, sys

"""
全局变量：很多封闭模块都要用或者有一定的固定含义
"""
# 服务器地址
ADDR = ("0.0.0.0", 8888)

# 存储结果{name:address}
user = {}


# 登入聊天室
def do_login(user_name, socket_, addr):
    if user_name in user or "管理员" in user_name:
        socket_.sendto("用户名已经存在。".encode(), addr)
        return
    socket_.sendto(b"OK", addr)  # 可以进入聊天室
    msg = "\n欢迎'%s'进入了聊天室" % user_name
    for name in user:
        socket_.sendto(msg.encode(), user[name])
    user[user_name] = addr  # 插入字典


# 聊天
def do_chat(socket_, name, text):
    msg = "\n%s:%s" % (name, text)
    for i in user:
        # 刨除其本人
        if i != name:
            socket_.sendto(msg.encode(), user[i])


# 退出
def do_quit(socket_, name):
    msg = "\n%s 退出聊天室" % name
    for i in user:
        if i != name:
            socket_.sendto(msg.encode(), user[i])
        else:
            socket_.sendto(b"EXIT", user[i])
    del user[name]  # 删除用户


# 处理请求
def do_request(s):
    while True:
        data, addr = s.recvfrom(1024)
        list_data = data.decode().split(" ")  # 拆分请求
        # 根据不同的请求类型具体执行不同的事情
        # L进入，C聊天，Q退出
        if list_data[0] == "L":
            do_login(list_data[1], s, addr)  # 执行具体工作
        elif list_data[0] == "C":
            text = " ".join(list_data[2:])
            do_chat(s, list_data[1], text)
        elif list_data[0] == "Q":
            do_quit(s, list_data[1])
        else:
            pass


# 搭建网络
def main():
    # udp服务端
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)

    pid = os.fork()
    if pid == 0:  # 子进程处理管理员消息
        while True:
            msg = input("管理员消息：")
            msg = "C 管理员 " + msg
            s.sendto(msg.encode(), ADDR)
    else:
        # 请求处理函数
        do_request(s)


main()
