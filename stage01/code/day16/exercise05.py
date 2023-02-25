"""
    练习：定义MyRange类，实现下列功能
    for item in range(10):
        print(item)
"""


class MyRange:
    def __init__(self, end_number):
        self.__end_number = end_number

    def __iter__(self):
        return MyRangeIterator(self.__end_number)


class MyRangeIterator:
    def __init__(self, end_number):
        self.__end_number = end_number
        self.__index = 0

    def __next__(self):
        if self.__index >= self.__end_number:
            raise StopIteration
        temp = self.__index
        self.__index += 1
        return temp


# next一次，计算一次，返回一次
for i in MyRange(10):
    print(i)
