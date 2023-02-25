"""
file_read.py
文件读取演示
"""

# 打开文件
f = open("text", "r", encoding="utf-8")

# while True:
#     # 读到文件结尾返回空字符串
#     data = f.read(32)  # 每次最多读100个字符
#     if not data:  # 读到结尾跳出循环
#         break
#     print(data)

# # 读取一行内容
# data = f.readline(10)  # 读取前10个字符
# print("一行内容", data)
# data = f.readline()  # 读完和一行剩余内容
# print("一行内容", data)

# # 将内容读取为列表，每行为列表一个元素
# data = f.readlines(18)  # 前18个字符所在的行作为读取对象
# print(data)

# f为可迭代对象
for i in f:
    print(i)  # 每次迭代到一行内容


# 关闭
f.close()
