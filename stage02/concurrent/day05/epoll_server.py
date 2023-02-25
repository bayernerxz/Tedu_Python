from socket import *
from select import *

# 创建监听套接字，作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8888))
s.listen(3)

# 创建epoll对象
ep = epoll()

# 建立查找字典，通过一个IO的fileno找到IO对象
# 始终根register的IO保持一致
fdmap = {s.fileno(): s}

# 关注s
ep.register(s, EPOLLIN | EPOLLERR)

# 循环监控IO发生
while True:
    events = ep.poll()  # 这个地方不变
    # 循环遍历列表，查看哪个IO就绪，进行处理
    for fd, event in events:
        # 区分哪个IO就绪
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("Connect from", addr)
            # 关注客户端连接套接字
            ep.register(c, EPOLLIN | EPOLLET)  # EPOLLET边缘触发
            fdmap[c.fileno()] = c  # 维护字典
        elif event & EPOLLIN:  # 判断是否是EPOLLIN就绪
            data = fdmap[fd].recv(1024).decode()
            if not data:
                ep.unregister(fd)  # 取消关注
                del fdmap[fd]  # 从字典删除
                continue
            print(data)
            fdmap[fd].send(b"OK")
