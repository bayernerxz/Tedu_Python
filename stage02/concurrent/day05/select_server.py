"""
select tcp服务
重点代码

思路分析:
1.将关注的I0放入到监控列表
2.当I0就绪时会通过select返回
3.遍历返回值列表，得知哪个IO就绪进行处理
"""

from socket import *
from select import select

# 创建监听套接字，作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8888))
s.listen(3)

# 设置关注列表
rlist = [s]  # s用于等待处理连接
wlist = []
xlist = []  # xlist在linux中没有定义，所以没有用

# 循环监控IO
while True:
    rs, ws, xs = select(rlist, wlist, xlist)

    # 便利返回值列表，处理就绪的IO
    for r in rs:
        if r is s:
            c, addr = r.accept()
            print("Connect from", addr)
            rlist.append(c)  # 增加新的IO关注
        else:
            # 有客户端发消息
            data = r.recv(1024).decode()
            # 客户端退出
            if not data:
                rlist.remove(r)  # 取消对客户端关注
                r.close()
                continue  # 因为rs里面可能有很多个c，当这个c操作完成后，还需要处理其他c，所以需要用continue只退出这一次循环
            print(data)
            # r.send(b"OK")  # 发送可以写在wlist中，作为写操作IO进行监控
            wlist.append(r)  # 给我发消息的客户端
    for w in ws:
        w.send(b"OK")
        wlist.remove(w)  # 发完消息移除
    for x in xs:
        pass
