"""
fork.py fork进程创建演示2
"""

import os
from time import sleep

print("="*50)
a = 1

pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    print("The new process")
    print("a=", a)
    a = 10000
else:
    print("The old process")
    print("a=", a)

print("All -->", a)
