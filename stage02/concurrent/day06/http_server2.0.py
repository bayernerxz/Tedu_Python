"""
httpserver v2.0
env:python3.10
io多路复用和训练
"""

from socket import *
from select import *


# 具体的功能实现
class HTTPServer:
    def __init__(self, host="0.0.0.0", port=8000, dir_=None):
        self.host = host
        self.port = port
        self.dir = dir_
        self.address = (host, port)
        # 多路复用列表
        self.rlist = []
        self.wlist = []
        self.xlist = []
        # 实例化对象时直接创建套接字
        self.__create_socket()
        self.__bind()

    # 创建套接字
    def __create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # 绑定地址
    def __bind(self):
        self.sockfd.bind(self.address)

    # 启动服务函数
    def server_forever(self):
        self.sockfd.listen(3)
        print("Listen the port %d" % self.port)
        # IO多路复用接收客户端请求
        self.rlist.append(self.sockfd)
        self.__handle_io_by_select()

    def __handle_io_by_select(self):
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    self.rlist.append(c)
                else:
                    self.__handle_link(r)
            # for w in ws:
            #     pass
            # for x in xs:
            #     pass

    def __handle_link(self, connfd):
        # 接收HTTP请求
        request = connfd.recv(4096)
        # 客户端断开
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return
        # 提取请求内容
        info = self.__get_request_info(request)
        print(connfd.getpeername(), ":", info)  # 获取连接的客户端地址
        self.__handle_request_info(connfd, info)

    @staticmethod
    def __get_request_info(request):
        request_line = request.splitlines()[0]  # 字节串按行切割。
        info = request_line.decode().split(" ")[1]
        return info

    def __handle_request_info(self, connfd, info):
        # 根据请求内容进行数据处理
        # 分为两类 1.请求网页 2.其他
        if info == "/" or info[-5:] == ".html":
            self.__get_html(connfd, info)
        else:
            self.__get_data(connfd)

    # 返回网页
    def __get_html(self, connfd, info):
        filename = self.__get_file_name(info)
        try:
            fd = open(filename, "r", encoding="utf-8")
        except Exception:
            # 网页不存在
            response = self.__generate_html_response(404)
        else:
            response = self.__generate_html_response(200, fd)
        finally:
            # 将响应发送给浏览器
            connfd.send(response.encode())

    def __get_file_name(self, info):
        if info == "/":
            # 请求主页
            filename = self.dir + "/index.html"
        else:
            filename = self.dir + info
        return filename

    @staticmethod
    def __generate_html_response(html_code, fd=None):
        response = HTTPServer.__generate_html_response_line(html_code)
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response = HTTPServer.__generate_html_response_body(fd, html_code, response)
        return response

    @staticmethod
    def __generate_html_response_body(fd, html_code, response):
        if html_code == 404:
            response += "<h1>Sorry...</h1>"
        elif html_code == 200:
            fd.read()
        return response

    @staticmethod
    def __generate_html_response_line(html_code):
        if html_code == 404:
            response = "HTTP/1.1 404 Not Found\r\n"
        elif html_code == 200:
            response = "HTTP/1.1 200 OK\r\n"
        return response

    @staticmethod
    # 其他数据
    def __get_data(connfd):
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Waiting for httpserver 3.0</h1>"
        connfd.send(response.encode())


if __name__ == '__main__':
    """
    通过HTTPServer类快速搭建服务，展示自己的网页
    """
    # 用户决定的参数
    HOST = "0.0.0.0"
    POST = 8000
    DIR = "./static"  # 网页存储位置

    httpd = HTTPServer(HOST, POST, DIR)  # 实例化对象
    httpd.server_forever()  # 启动服务
