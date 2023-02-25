"""
使用udp完成，客户端不断录入学生信息，将其发送到服务端，
在服务端，将学生信息写入到一个文件中，每个学生信息占一行。
信息格式：id     name    age     score
* id(int)   name(str)   age(int)    score(float)
"""

from socket import *
import struct

# 和客户端一致
st = struct.Struct("i32sif")

# udp套接字
sockfd = socket(AF_INET, SOCK_DGRAM)
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(("0.0.0.0", 10050))

# 打开文件
f = open("student.txt", "a")

while True:
    data, addr = sockfd.recvfrom(1024)
    # (1, b"Lily", 14, 92.5)
    data = st.unpack(data)

    # 写入文件
    info = "%d    %-10s    %d    %.1f\n" % data
    f.write(info)
    f.flush()
