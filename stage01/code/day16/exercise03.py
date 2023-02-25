# 练习：图形管理器记录多个图形
#       迭代图形管理器对象

class Graphic:
    pass


class GraphicManager:
    """
        图形管理器，可迭代对象
    """
    def __init__(self):
        self.__graphic_list = []

    def add_graphic(self, graphic):
        self.__graphic_list.append(graphic)

    def __iter__(self):
        return GraphicIterator(self.__graphic_list)


class GraphicIterator:
    """
        图形迭代器（获取下一个数据）
    """
    def __init__(self, graphic_list):
        self.__graphic_list = graphic_list
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__graphic_list)-1:
            raise StopIteration
        temp = self.__graphic_list[self.__index]
        self.__index += 1
        return temp


m01 = GraphicManager()
m01.add_graphic(Graphic())
m01.add_graphic(Graphic())
m01.add_graphic(Graphic())

for item in m01:
    print(item)
