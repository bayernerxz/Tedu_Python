"""
lstack.py 栈的链式
重点代码

思路分析：
1.源于链表结构
2.封装栈的操作方法（入栈，出栈，栈空，栈顶元素
3.链表的开头作为栈顶？（不用每次遍历）

"""


# 自定义异常
class StackError(Exception):
    pass


# 创建节点类
class Node:
    """
    思路：将自定义的为视为节点的生成类，实例对象中包含数据部分和指向下一个节点的next
    """

    def __init__(self, val, next_=None):
        self.val = val  # 有用数据
        self.next = next_  # 循环下一个节点关系


# 链式栈操作
class LStack:
    def __init__(self):
        # 标记栈顶位置
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self, val):
        # node = Node(val)
        # node.next = self._top
        # self._top = node
        self._top = Node(val, self._top)

    def pop(self):
        if self.is_empty():
            raise StackError("Stack is empty.")
        result = self._top.val
        self._top = self._top.next
        return result

    def top(self):
        if self.is_empty():
            raise StackError("Stack is empty.")
        return self._top.val


if __name__ == "__main__":
    st = LStack()  # 初始化栈
    st.push(10)
    st.push(20)
    st.push(30)
    while not st.is_empty():
        print(st.pop())
