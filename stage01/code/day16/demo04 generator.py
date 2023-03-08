"""
    yield --> 生成器
"""

"""
class MyRange:
    def __init__(self, end_number):
        self.__end_number = end_number

    def __iter__(self):
        number = 0
        while number < self.__end_number:
            yield number
            number += 1

my01 = MyRange(10)
iterator = my01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
"""

"""
# 生成器原理
class MyGenerator:
    '''
        生成器=可迭代对象+迭代器
    '''

    def __init__(self, end):
        self.begin = 0
        self.end = end

    def __iter__(self):
        return self.begin

    def __next__(self):
        if self.begin >= self.end:
            raise StopIteration
        temp = self.begin
        self.begin += 1
        return temp
"""


def my_range(stop_value):
    number = 0
    while number < stop_value:
        yield number
        number += 1


my01 = my_range(10)

print(type(my01), dir(my01))  # <class 'generator'>

print(id(my01.__iter__()), id(my01))  # 地址相同

for item in my_range(10):
    print(item)
