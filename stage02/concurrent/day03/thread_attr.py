"""
thread_attr.py
线程属性演示
"""

from threading import Thread
from time import sleep


def fun():
    sleep(3)
    print("线程属性测试")


t = Thread(target=fun, name="Doif")

t.setDaemon(True)  # 主线程退出分支线程也退出

t.setName("Deuf")
print("Name:", t.getName())
print("is alive:", t.is_alive())
print("daemon:", t.isDaemon())
