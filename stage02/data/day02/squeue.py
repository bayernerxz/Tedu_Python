"""
squeue.py 队列模型的顺序存储

思路分析：
1.基于列表完成数据存储
2.通过封装规定数据操作
3.先确定列表的哪一端作为队头
"""
from sstack import *


# 自定义队列异常
class QueueError(Exception):
    pass


# 顺序队列类
class SQueue:
    def __init__(self):
        # 空列表就是队的存储空间
        # 列表的最后一个元素作为队头
        self._elements = []

    # 判断列表是否为空
    def is_empty(self):
        return self._elements == []

    # 入队
    def enqueue(self, val):
        self._elements.append(val)

    # 出队 列表的第一个元素出
    def dequeue(self):
        if self.is_empty():
            raise QueueError("Stack is empty")
        return self._elements.pop(0)  # 弹出并返回

    # 查看队头元素
    def front(self):
        if self.is_empty():
            raise QueueError("Stack is empty")
        return self._elements[0]

    # 查看队尾元素
    def rear(self):
        if self.is_empty():
            raise QueueError("Stack is empty")
        return self._elements[-1]


if __name__ == "__main__":
    sq = SQueue()  # 初始化队列
    for i in range(10):
        sq.enqueue(i)

    # 反转队列
    st = SStack()
    # 循环出队入栈
    while not sq.is_empty():
        st.push(sq.dequeue())
    # 循环出栈入队
    while not st.is_empty():
        sq.enqueue(st.pop())

    while not sq.is_empty():
        print(sq.dequeue())
