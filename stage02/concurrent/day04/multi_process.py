from test import *
from multiprocessing import Process, freeze_support
import time

if __name__ == "__main__":
    freeze_support()
    jobs = []
    tm = time.time()

    for i in range(10):
        p = Process(target=io)
        jobs.append(p)
        p.start()
    for i in jobs:
        i.join()

    print("Single CPU:", time.time() - tm)  # count() 1.7s  io() 2.1s
