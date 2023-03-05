"""
HTTPServer部分的主程序
    获取http请求
    解析http请求
    将请求发给WebFrame
    从WebFrame接收反馈数据
    将数据组织为Response格式发送给客户端
"""

from socket import *
import sys
from threading import Thread
from config import *
import re
import json

# 服务器地址
ADDR = (HOST, PORT)


# 和web frame通信的函数
def connect_frame(env):
    s = socket()
    try:
        s.connect((frame_ip, frame_port))
    except Exception as e:
        print(e)
        return
    # 将字典转化为json字符串
    data = json.dumps(env)
    # 将解析后的请求发送给webframe
    s.send(data.encode())
    # 接受来自webframe数据
    data = s.recv(4096 * 100).decode()
    return json.loads(data)


# 将httpserver基本功能封装为类
class HTTPServer:
    def __init__(self):
        self.address = ADDR
        self.create_socket()  # 和浏览器交互
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.address)
        self.ip = self.address[0]
        self.port = self.address[1]

    # 启动服务
    def serve_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %d" % self.port)
        while True:
            connfd, addr = self.sockfd.accept()
            print("Connect from", addr)
            client = Thread(target=self.handle, args=(connfd,))
            client.setDaemon(True)
            client.start()

    # 具体处理客户端请求任务
    def handle(self, connfd):
        # 获取HTTP请求
        request = connfd.recv(4096).decode()
        pattern = r"^(?P<method>[A-Z]+)\s(?P<info>+/\S*)"
        try:
            env = re.match(pattern, request).groupdict()
        except:
            # 客户端断开
            connfd.close()
            return
        else:
            data = connect_frame(env)
            if data:
                self.response(connfd, data)

    # 给浏览器发送数据
    @staticmethod
    def response(connfd, data):
        # data --> {"status":"200", "data":"xxxx"}
        if data["status"] == "200":
            response_headers = "HTTP/1.1 200 OK\r\n"
            response_headers += "Content-Type:text/html\r\n"
            response_headers += "\r\n"
            response_body = data["data"]

        elif data["status"] == "404":
            response_headers = "HTTP/1.1 404 Not Found\n"
            response_headers += "Content-Type:text/html\r\n"
            response_headers += "\r\n"
            response_body = data["data"]

        # elif data["status"] == "500":
        #     pass

        # 给浏览器发送数据
        response_data = response_headers + response_body
        connfd.send(response_data.encode())


httpd = HTTPServer()
httpd.serve_forever()