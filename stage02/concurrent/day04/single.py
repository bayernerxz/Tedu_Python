from test import *
import time

tm = time.time()

for i in range(10):
    # count(1, 1)
    io()

print("Single CPU:", time.time() - tm)  # count() 4.6s io() 6.3s
