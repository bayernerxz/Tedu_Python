"""
array.py
共享内存存放一组数据
"""

from multiprocessing import Process, Array, freeze_support

# 创建共享内存
# shm = Array("i", [1, 2, 3, 4])
# shm = Array("i", 5)  # 初始开辟5个整形空间，初始化的元素每一位都默认为0
shm = Array("c", b"hello")  # 字节串


def fun(shm):
    # array 创建共享内存对象可迭代
    for i in shm:
        print(i)
    # shm[1] = 1000
    shm[1] = b"H"  # 修改共享内存


if __name__ == "__main__":
    freeze_support()
    p = Process(target=fun, args=(shm,))
    p.start()
    p.join()
    for i in shm:
        print(i)

    print(shm.value)  # 打印字节串
