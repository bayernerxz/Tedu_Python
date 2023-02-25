from socket import *
import struct

sockfd = socket(AF_INET, SOCK_DGRAM)
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(("0.0.0.0", 10050))

while True:
    file = open("stu_info.txt", "a", encoding="utf-8")
    info = sockfd.recvfrom(1024)[0]
    stu_id, name, age, score = struct.unpack("i16sif", info)
    str_name = ""
    for i in name:
        if i:
            str_name += chr(i)
        else:
            break

    file.write("%d\t%s\t%d\t%0.1f\n" % (stu_id, str_name, age, score))
    file.close()
