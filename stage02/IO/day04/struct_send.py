"""
使用udp完成，客户端不断录入学生信息，将其发送到服务端，
在服务端，将学生信息写入到一个文件中，每个学生信息占一行。
信息格式：id     name    age     score
* id(int)   name(str)   age(int)    score(float)
"""

from socket import *
import struct

# 数据格式定义
st = struct.Struct("i32sif")

# udp套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

while True:
    print("=" * 50)
    stu_id = int(input("ID:"))
    name = input("Name:").encode()
    age = int(input("Age:"))
    score = float(input("Score:"))
    # 打包数据发送
    data = st.pack(stu_id, name, age, score)
    sockfd.sendto(data, ("127.0.0.1", 8888))