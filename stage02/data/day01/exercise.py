"""
创建两个链表，两个链表中的值均为有序值，将两个链表合并为一个，合并后要求值仍为有充值。
"""

from link_list import *
from common.list_helper import ListHelper


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

    def merge(self, obj, func=lambda i: i):
        """
        将obj与self实例对象进行合并，并仍按一定顺序形成有序链表
        :param obj: 需要合并的链表，其元素的数值需要与当前self实例对象一致
        :param func: 传入需要排序时需要比较的方法，默认是直接对数值进行排序。
        """
        tmp_list = []
        for i in range(self.count()):
            tmp_list.append(self.get_index(i))
        for i in range(obj.count()):
            tmp_list.append(obj.get_index(i))
        ListHelper.sort_ascending(tmp_list, func)
        self.init_list(tmp_list)


list01 = OrderedLinkList([1, 2, 6, 3, 7, 9])
list02 = OrderedLinkList([4, 5, 8, 10])

list01.merge(list02)
list01.show()
