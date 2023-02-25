"""
编写一个文件拷贝程序，从终端输入一个文件，将文件保存在当前目录下。如果文件不存在则提示。
    * 文件类型不确定（可能是文本文件，可能是二进制文件）
    * 边读边写
"""

file_path = input("请输入文件路径：")

if "/" in file_path:
    file_name = file_path.split("/")[-1]
else:
    file_name = file_path

source = open(file_path, "rb")
replica = open("./" + file_name, "wb")

while True:
    data = source.read(100)
    if data == b'':
        break
    replica.write(data)

source.close()
replica.close()
