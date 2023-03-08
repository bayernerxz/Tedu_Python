"""
    迭代器 --> yield
    练习：将迭代器版本的图形管理器改为yield版本。
"""


class MyRange:
    def __init__(self, end_number):
        self.__end_number = end_number

    def __iter__(self):
        # return MyRangeIterator(self.__end_number)
        # 0 --> self.__end_number
        # yield作用：将下列代码改为迭代器模式的代码。
        # 生成迭代器代码的大致规则：
        # 1.将yield之前的语句定义在next方法中
        # 2.将yield后面的数据作为next方法返回值
        number = 0
        while number < self.__end_number:
            yield number
            number += 1

        # print("准备数据")
        # yield 0
        # print("准备数据")
        # yield 1
        # print("准备数据")
        # yield 2


"""
class MyRangeIterator:
    def __init__(self, end_number):
        self.__end_number = end_number
        self.__number = 0

    def __next__(self):
        if self.__number >= self.__end_number:
            raise StopIteration
        temp = self.__number
        self.__number += 1
        return temp
"""

# next一次，计算一次，返回一次
# for i in MyRange(10):
#     print(i)

my01 = MyRange(10)
iterator = my01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
