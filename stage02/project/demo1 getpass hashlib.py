"""
    demo1 getpass.py
    getpass()的作用类似于input(),只不过输入的字符串不会显示出来。
    hashlib 加密演示
    hashlib模块内的方法还有sha1,sha256等等用于加密
"""

import getpass  # 隐藏输入
import hashlib  # 转换加密

# 输入隐藏
pwd = getpass.getpass("PW:")
print(pwd)

# hash对象
# hash=hashlib.md5()  # 生成对象

# 算法加盐(例如是#$awv3_，这个key和用户密码混合后再加密)
hash = hashlib.md5("*#06#".encode())

hash.update(pwd.encode())  # 算法加密
pwd = hash.hexdigest()  # 提取加密后的密码
print(pwd)
