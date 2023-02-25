"""
link_list.py
功能：实现单链表的构建和功能操作
重点代码
"""

from common.list_helper import ListHelper


# 创建节点类
class Node:
    """
    思路：将自定义的为视为节点的生成类，实例对象中包含数据部分和指向下一个节点的next
    """

    def __init__(self, val, next_=None):
        self.val = val  # 有用数据
        self.next = next_  # 循环下一个节点关系
    #
    # def __lt__(self, other):
    #     return self.val < other.val
    #
    # def __le__(self, other):
    #     if self.val <= other.val:
    #         return True
    #     else:
    #         return False
    #
    # def __eq__(self, other):
    #     if self.val == other.val:
    #         return True
    #     else:
    #         return False
    #
    # def __ne__(self, other):
    #     if self.val != other.val:
    #         return True
    #     else:
    #         return False
    #
    # def __gt__(self, other):
    #     if self.val > other.val:
    #         return True
    #     else:
    #         return False
    #
    # def __ge__(self, other):
    #     if self.val >= other.val:
    #         return True
    #     else:
    #         return False


class LinkList:
    """
    思路：单链表类，生成对象可以进行增删改查操作
        具体操作通过调用具体方法完成
    """

    def __init__(self, iterable=None):
        """
        初始化链表，标记一个链表的开端，以便于获取后续的节点
        """
        self.head = Node(None)
        if iterable:
            tmp_list = list(iterable)
            self.init_list(tmp_list)

    # 通过list_为链表添加一组节点
    def init_list(self, list_):
        tmp = self.head  # p作为移动变量
        for item in list_:
            tmp.next = Node(item)
            tmp = tmp.next

    # 遍历链表
    def show(self):
        tmp = self.head.next  # 第一个有效节点
        while tmp is not None:
            print(tmp.val)
            tmp = tmp.next

    # 判断链表为空
    def is_empty(self):
        if self.head.next is None:
            return True
        return False

    # 清空链表
    def clear(self):
        self.head.next = None

    # 尾部插入
    def append(self, val):
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = Node(val)

    # 头部插入
    def head_insert(self, val):
        # node = Node(val)
        # node.next = self.head.next
        # self.head.next = node
        self.head.next = Node(val, self.head.next)

    # 指定插入位置
    def insert(self, index, val):
        tmp = self.head
        for i in range(index):
            # 超出位置最大范围结束循环，插入到最后
            if tmp.next is None:
                break
            tmp = tmp.next
        # node = Node(val)
        # node.next = tmp.next
        # tmp.next = node
        tmp.next = Node(val, tmp.next)

    # 删除节点-按索引
    def delete_by_index(self, index):
        tmp = self.head
        for i in range(index - 1):
            if tmp.next is None:
                break
            tmp = tmp.next
        tmp.next = tmp.next.next

    # 删除节点-按值
    def delete(self, value):
        tmp = self.head
        # 结束循环必然两个条件其一为假
        while tmp.next and tmp.next.val != value:  # 短路原则，当and判断时只要有一个为False，就退出。
            tmp = tmp.next
        if tmp.next.next is None:
            raise ValueError(f"{value} not in link list.")
        else:
            tmp.next = tmp.next.next

    # 获取某个节点值，传入节点位置获取节点值
    def get_index(self, index):
        if index < 0:
            raise IndexError("index can not be negative.")
        tmp = self.head.next
        for i in range(index):
            if tmp.next is None:
                raise IndexError("index out of range.")
            tmp = tmp.next
        return tmp.val

    # 按节点位置更改值。
    def change_by_index(self, index, value):
        if index < 0:
            raise IndexError("index can not be negative.")
        tmp = self.head.next
        for i in range(index):
            if tmp.next is None:
                raise IndexError("index out of range.")
            tmp = tmp.next
        tmp.val = value

    # 获取节点数量（除head）：
    def count(self):
        result = 0
        p = self.head
        while p.next is not None:
            result += 1
            p = p.next
        return result


class OrderedLinkList(LinkList):
    """
    从链表类继承的，有序链表类。
    """

    def init_list(self, list_, func=lambda i: i):
        """
        构造有序链表
        :param list_:把list_中的元素作为链表的元素
        :param func:传入需要排序时需要比较的方法，默认是直接对数值进行排序。
        """
        tmp = self.head  # p作为移动变量
        ListHelper.sort_ascending(list_, func)
        for item in list_:
            tmp.next = Node(item)
            tmp = tmp.next

    def merge(self, obj):
        """
        将obj与self实例对象进行合并，并仍按一定顺序形成有序链表
        :param obj: 需要合并的链表，其元素的数值需要与当前self实例对象一致
        """
        # 下面的方法会额外开一个tmp_list的列表空间，需要在方法定义时传参func=lambda i:i
        # tmp_list = []
        # for i in range(self.count()):
        #     tmp_list.append(self.get_index(i))
        # for i in range(obj.count()):
        #     tmp_list.append(obj.get_index(i))
        # ListHelper.sort_ascending(tmp_list, func)
        # self.init_list(tmp_list)

        # 为了不额外开辟空间，会使用下面的方法
        reference_node_1 = self.head
        reference_node_2 = obj.head.next
        # 参考结点1.next只要不是None，就一直可以循环
        while reference_node_1.next is not None:
            reference_node_1, reference_node_2 = self.__process_ref_node_1(reference_node_1, reference_node_2)
        reference_node_1.next = reference_node_2

    @staticmethod
    def __process_ref_node_1(reference_node_1, reference_node_2):
        if reference_node_1.next.val < reference_node_2.val:
            reference_node_1 = reference_node_1.next
        else:
            reference_node_1, reference_node_2 = OrderedLinkList.__continue_ref_node(reference_node_1, reference_node_2)
        return reference_node_1, reference_node_2

    @staticmethod
    def __continue_ref_node(reference_node_1, reference_node_2):
        tmp_node = reference_node_1.next
        reference_node_1.next = reference_node_2
        reference_node_2 = tmp_node
        reference_node_1 = reference_node_1.next
        return reference_node_1, reference_node_2


if __name__ == "__main__":
    # node1 = Node(1)
    # node2 = Node(2, node1)  # node2.next == node1
    # node3 = Node(3, node2)  # node3.next == node2

    # list01 = LinkList()
    l1 = LinkList([2, 4, 5, 6, 8])
    # list01.init_list([1, 2, 3, 4, 5])
    # list01.head_insert(0)
    # list01.insert(0, 0)
    # list01.show()
    print(l1.count())
