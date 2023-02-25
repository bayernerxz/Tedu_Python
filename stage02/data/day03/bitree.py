"""
二叉树的简单实践

思路分析：
1.使用链式存储，一个Node表示一个树的节点
2.节点考点使用两个属性变量分别表示左连接和右连接
"""

from squeue import *


# 二叉树节点
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 二叉树的遍历类
class BiTree:
    def __init__(self, root=None):
        self.root = root

    # 先序遍历
    def __pre_order_by_node(self, node):
        if node is None:  # 终止条件
            return
        print(node.val, end=" ")
        self.__pre_order_by_node(node.left)
        self.__pre_order_by_node(node.right)

    def pre_order(self):
        self.__pre_order_by_node(self.root)

    def pre_order_by_node(self, node):
        self.__pre_order_by_node(node)

    # 中序遍历
    def __mid_order_by_node(self, node):
        if node is None:  # 终止条件
            return
        self.__mid_order_by_node(node.left)
        print(node.val, end=" ")
        self.__mid_order_by_node(node.right)

    def mid_order(self):
        self.__mid_order_by_node(self.root)

    def mid_order_by_node(self, node):
        self.__mid_order_by_node(node)

    # 后序遍历
    def __post_order_by_node(self, node):
        if node is None:  # 终止条件
            return
        self.__post_order_by_node(node.left)
        self.__post_order_by_node(node.right)
        print(node.val, end=" ")

    def post_order(self):
        self.__post_order_by_node(self.root)

    def post_order_by_node(self, node):
        self.__post_order_by_node(node)

    # 层次遍历
    @staticmethod
    def __level_order_by_node(node):
        """
        让初始节点先入队，谁出队就遍历谁，并且让它的左右孩子分别入队，直到队列为空。
        """
        sq = SQueue()
        sq.enqueue(node)  # 初始节点入队
        while not sq.is_empty():
            node = sq.dequeue()
            # 打印出队元素
            print(node.val, end=" ")
            if node.left:
                sq.enqueue(node.left)
            if node.right:
                sq.enqueue(node.right)

    def level_order(self):
        self.__level_order_by_node(self.root)

    def level_order_by_node(self, node):
        self.__level_order_by_node(node)


if __name__ == "__main__":
    # B F G D H I E C A
    # 根据后续遍历构建二叉树
    b = Node("B")
    f = Node("F")
    g = Node("G")
    d = Node("D", f, g)
    h = Node("H")
    i = Node("I")
    e = Node("E", h, i)
    c = Node("C", d, e)
    a = Node("A", b, c)  # 根节点

    # 将a作为遍历的起始位置
    bt = BiTree(a)
    bt.pre_order()
    print("=" * 20)
    bt.mid_order()
    print("=" * 20)
    bt.post_order()
    print()
    bt.level_order()
