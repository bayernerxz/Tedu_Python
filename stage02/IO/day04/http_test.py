"""
http 请求响应测试
可以在浏览器中用127.0.0.1:8000进行测试
"""

from socket import *

# http使用tcp传输
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8000))
s.listen(3)

c, addr = s.accept()
print("Connect from", addr)
data = c.recv(4096)  # 接收http请求
print(data.decode())

response = """HTTP/1.1 200 OK
Content_Type:text/html

<h1>Hello World</h1>
"""

c.send(response.encode())

c.close()
s.close()
