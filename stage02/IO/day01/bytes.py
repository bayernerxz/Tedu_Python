s = "hello"  # 字符串
print(s)

s = b"hello"  # 字节串，只有ascii字符才能加b转换
print(s)

"""
所有字符串都能够转换为字节串
但是并不是所有的字节串都能转换为字符串
"""

s = "你好".encode()  # 将字符串转换为字节串
print(s)

# 字节串转换为字符串
s = b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode()
print(s)
