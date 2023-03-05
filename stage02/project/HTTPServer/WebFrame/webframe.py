"""
webframe.py 模拟后端应用工作流程

从httpserver接受具体请求
根据请求进行逻辑处理和数据处理
将需要的数据反馈给httpserver
"""

import json
from socket import *
from settings import *
from select import select
from urls import *


# 应用类，处理某一方面的请求
class Application:
    def __init__(self):
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)
        self.sockfd.bind((frame_ip, frame_port))

    # 启动服务
    def start(self):
        self.sockfd.listen(5)
        print("Start app listen %s" % frame_port)
        self.rlist.append(self.sockfd)
        # select监控请求
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:
                    connfd, addr = r.accept()
                    self.rlist.append(connfd)
                else:
                    self.handle(r)
                    self.rlist.remove(r)

    # 处理具体的httpserver请求
    def handle(self, connfd):
        request = connfd.recv(1024).decode()
        request = json.loads(request)
        # request--> {"method":"GET","info":"/"}
        if request["method"] == "GET":
            if request['info'] == "/" or request["info"][-5:] == ".html":
                response = self.get_html(request["info"])
            else:
                response = self.get_data(request["info"])
        elif request["method"] == "POST":
            pass
        # 将数据发送给httpserver
        # response=>{"status":"200","data":"xxx"}
        response = json.dumps(response)
        connfd.send(response.encode())
        connfd.close()

    def get_html(self, info):
        if info == "/":
            filename = STATIC_DIR + "/index.html"
        else:
            filename = STATIC_DIR + info
        try:
            fd = open(filename, "r", encoding="utf-8")
        except Exception as e:
            fd = open(STATIC_DIR + "/404.html")
            return {"status": "404", "data": fd.read()}
        else:
            return {"status": "200", "data": fd.read()}

    # 处理数据
    def get_data(self, info):
        for url, func in urls:
            if url == info:
                return {"status": "200", "data": func()}
        return {"status": "404", "data": "Sorry..."}


app = Application()
app.start()  # 启动应用服务

# sockfd = socket()
# sockfd.bind(("0.0.0.0", 8080))
# sockfd.listen(3)
#
# while True:
#     c, addr = sockfd.accept()
#     data = c.recv(1024).decode()
#     print(json.loads(data))
#     d = {"status": "200", "data": "xxxxxxx"}
#     c.send(json.dumps(d).encode())
