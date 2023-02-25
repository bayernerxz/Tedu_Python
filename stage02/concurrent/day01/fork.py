"""
fork.py fork进程创建演示1
"""
import os
from time import sleep

# 创建子进程
pid = os.fork()  # os.fork()只能再linux或者unix下使用，windows下需要使用multiprocessing模块下的Process类

if pid < 0:
    print("Create process failed")
# 子进程执行部分
elif pid == 0:
    sleep(3)
    print("The new process")
# 父进程执行部分
else:
    sleep(4)  # 如果是一个进程执行需要7s，但是这样多进程执行，只需要4s
    print("The old process")
# 父子进程都会执行
print("Fork test over")
