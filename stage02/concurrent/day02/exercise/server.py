from socket import *
import struct


def enter_group(data_):
    info = data[0] + "加入了聊天室"
    for item in list_client_ip:
        sockfd.sendto(info.decode(), item)


SERVER_IP = ("0.0.0.0", 10050)
FORMAT = "10s1024s"  # 传输格式分为两部分，10s是用户名，1024s是消息内容。

sockfd = socket(AF_INET, SOCK_DGRAM)
sockfd.bind(SERVER_IP)

list_client_ip = []

while True:
    try:
        data, addr = sockfd.recvfrom(1024)
        list_data = struct.unpack(FORMAT, data)
        enter_group(data)
        list_client_ip.append(addr)
    except Exception:
        break
