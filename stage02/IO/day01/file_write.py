"""
file_write.py
文件写操作演示
"""

# # 打开文件
# f = open("test", "w", encoding="utf-8")
#
# # 写操作
# f.write("hello 死鬼\n")  # 如果没有手动加\n，那么与下一行是在同一行中
# f.write("哎呀，干啥")

# # 打开文件
# f = open("test", "wb")
#
# # 写操作
# f.write("hello 死鬼\n".encode())
# f.write("哎呀，干啥".encode())

# # 打开图片
# f = open("./img/text.JPG", "wb")
#
# # 写操作
# f.write("hello 死鬼\n".encode())
# f.write("哎呀，干啥".encode())  # jpg格式文件，识别不了加入进的内容

# # 将列表写入 人为添加换行
# f = open("test", "w", encoding="utf-8")
# l = ["hello world\n", "哈哈哈"]
# f.writelines(l)

# 追加方式
f = open("test", "a", encoding="utf-8")
l = ["hello world\n", "哈哈哈"]
f.writelines(l)

f.close()
