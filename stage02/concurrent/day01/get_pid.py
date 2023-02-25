"""
获取进程PID号
"""

import os
from time import sleep

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    sleep(1)  # 在sleep之后，子进程成为孤儿进程，被系统接管
    print("Child PID:", os.getpid())  # 子PID
    print("Get parent PID:", os.getppid())  # 父PID
else:
    print("Get child PID:", pid)  # 子PID
    print("Parent PID:", os.getpid())  # 父PID
