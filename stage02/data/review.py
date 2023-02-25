# 创建节点类
class Node:
    """
    思路：将自定义的为视为节点的生成类，实例对象中包含数据部分和指向下一个节点的next
    """

    def __init__(self, val, next_=None):
        self.val = val  # 有用数据
        self.next = next_  # 循环下一个节点关系


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
        if tmp.next is None:
            raise ValueError(f"{value} not in link list.")
        else:
            tmp.next = tmp.next.next

    # 按值获取第一个值等于该节点的索引
    def get_index(self, value):
        tmp = self.head
        count = 0
        # 结束循环必然两个条件其一为假
        while tmp.next and tmp.next.val != value:  # 短路原则，当and判断时只要有一个为False，就退出。
            tmp = tmp.next
            count += 1
        if tmp.next is None:
            raise ValueError(f"{value} not in link list.")
        else:
            return count

    # 获取某个节点值，传入节点位置获取节点值
    def get_value_by_index(self, index):
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
