"""
lqueue.py 栈的链式
重点代码

思路分析：
1.基于链表构建队列模型
2.链表的开端作为队头，结尾位置作为队尾
3.单独定义队尾标记，避免每次插入数据遍历
4.队头和队尾重叠认为队列为空
"""


# 自定义队列异常
class QueueError(Exception):
    pass


# 创建节点类
class Node:
    """
    思路：将自定义的为视为节点的生成类，实例对象中包含数据部分和指向下一个节点的next
    """

    def __init__(self, val, next_=None):
        self.val = val  # 有用数据
        self.next = next_  # 循环下一个节点关系


# 队列操作
class LQueue:
    def __init__(self):
        # 定义队头和队尾的属性变量
        self._rear = self._front = Node(None)

    def is_empty(self):
        return self._front is self._rear

    # 入队 rear动
    def enqueue(self, val):
        self._rear.next = Node(val)
        self._rear = self._rear.next

    # 出队 front动
    def dequeue(self):
        if self.is_empty():
            raise QueueError("Queue is empty.")
        result = self._front.next.val
        self._front = self._front.next
        return result

    def front(self):
        if self.is_empty():
            raise QueueError("Queue is empty.")
        return self._front.next.val

    def rear(self):
        if self.is_empty():
            raise QueueError("Queue is empty.")
        return self._rear.val


if __name__ == "__main__":
    lq = LQueue()  # 初始化队列
    for i in range(10):
        lq.enqueue(i)

    while not lq.is_empty():
        print(lq.dequeue())
