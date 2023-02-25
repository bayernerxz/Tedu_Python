from test import *
from threading import Thread
import time

if __name__ == "__main__":
    jobs = []
    tm = time.time()

    for i in range(10):
        p = Thread(target=count, args=(1, 1))
        jobs.append(p)
        p.start()
    for i in jobs:
        i.join()

    print("Single CPU:", time.time() - tm)  # count() 4.5s  io() 6.8s
