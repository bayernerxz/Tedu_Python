"""
空洞文件
"""

f = open("test", "wb")

f.write(b"start")
f.seek(1024 * 1024, 2)  # 从结尾移动1M字节
f.write(b"end")

f.close()
