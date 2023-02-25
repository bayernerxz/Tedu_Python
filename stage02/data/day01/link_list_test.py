from link_list import *
from time import time

tm = time()

list01 = list(range(6))

l = LinkList()
l.init_list(list01)

print(l.get_index(5))
l.show()

print("time:", time() - tm)
