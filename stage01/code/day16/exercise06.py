"""
    练习：将迭代器版本的图形管理器改为yield版本。
"""


class Graphic:
    pass


class GraphicManager:
    """
        图形管理器，可迭代对象（参与for）
    """

    def __init__(self):
        self.__graphic_list = []

    def add_graphic(self, graphic):
        self.__graphic_list.append(graphic)

    def __iter__(self):
        # 执行过程：
        # 1.调用当前方法，不执行（内部创建迭代器对象）
        # 2.调用__next__()方法，才执行
        # 3.再次执行yield语句，暂时离开。
        # 4.再次调用__next__()方法，继续执行
        # 5.重复第3/4步骤，直至

        # index = 0
        # while index < len(self.__graphic_list):
        #     yield self.__graphic_list[index]
        #     index += 1

        # for i in range(len(self.__graphic_list)):
        #     yield self.__graphic_list[i]

        for item in self.__graphic_list:
            yield item


m01 = GraphicManager()
m01.add_graphic(Graphic())
m01.add_graphic(Graphic())
m01.add_graphic(Graphic())

for item in m01:
    print(item)
