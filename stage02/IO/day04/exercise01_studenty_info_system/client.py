from socket import *
import struct

sockfd = socket(AF_INET, SOCK_DGRAM)

stu_id = 1
while True:
    name = input("Name:").encode()
    if not name:
        break
    age = int(input("age:"))
    score = float(input("score:"))
    stu_info = struct.pack("i16sif", stu_id, name, age, score)
    sockfd.sendto(stu_info, ("127.0.0.1", 10050))
    stu_id += 1
sockfd.close()
