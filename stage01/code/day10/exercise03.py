"""
    练习：定义对象计数器
    定义老婆类，创建3个老婆对象。
    可以通过类变量记录老婆对象个数，可以通过类方法打印老婆对象个数。
"""


class Wife:
    count = 0

    @classmethod
    def print_count(cls):
        print("老婆共有%d个" % cls.count)

    def __init__(self, name):
        self.name = name
        Wife.count += 1


w01 = Wife("双儿")
w02 = Wife("苏荃")
w03 = Wife("小郡主")
Wife.print_count()
