from socket import *
from time import sleep


def get_name(file):
    return file.split("/")[-1]


def read_data(file):
    with open(file, "rb") as f:
        return f.read()


sockfd = socket()
sockfd.connect(("127.0.0.1", 8888))
str_file = input("File>>")
data = get_name(str_file)
sockfd.send(data.encode())
sleep(0.1)
data = read_data(str_file)
sockfd.send(data)
sockfd.close()
