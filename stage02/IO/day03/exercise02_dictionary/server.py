from socket import *


def consult_dict(key):
    f = open("dict2.txt", encoding="utf-8")
    for line in f:
        w = line.split(" ")[0]
        if w > key:
            return ""
        elif w == key:
            return line
    else:
        return ""


sockfd = socket(AF_INET, SOCK_DGRAM)
sockfd.bind(("127.0.0.1", 8888))
while True:
    try:
        word, addr = sockfd.recvfrom(1024)
        interpretation = consult_dict(word.decode())
        print("正在为%s:%s查询的单词是：%s" % (addr[0], addr[1], word.decode()))
        if interpretation:
            print("找到%s的解释" % word.decode())
            sockfd.sendto(interpretation.encode(), addr)
        else:
            print("没有找到%s的解释" % word.decode())
            sockfd.sendto("没有单词".encode(), addr)
    except Exception:
        break

sockfd.close()
