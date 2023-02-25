"""
编写一个程序，向一个文件中写入如下内容：
    1. 2019-1-1 18：18：18
    2. 2019-1-1 18：18：19

    3. 2019-1-1 18：18：24
    每隔1s写入一次，序号从1排列
    ctrl+C结束程序，下次启动程序，序号要与之前的衔接。
"""

import time


def get_time_info(index_):
    # 获得当前时间时间戳
    now = int(time.time())  # 这是时间戳
    # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    time_array = time.localtime(now)
    other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return str(index_) + ". " + other_style_time + "\n"


f = open("record.txt", "r+", encoding="utf-8")

index = 0
for line in f:
    index = int(line.split(".")[0])

try:
    while True:
        index += 1
        f.write(get_time_info(index))
        time.sleep(1)
except Exception:
    f.close()
