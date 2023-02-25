"""
    复习
        View    Model       Controller
        界面      数据        业务逻辑
        变化      载体         变化
"""


class XXController:
    def __init__(self):
        self.__stu_list = []

    def add_xx(self, a):
        print("Controller add data:", a)


class XXView:
    def __init__(self):
        self.__c = XXController()

    def input_xx(self):
        # 需求：调用XXController类中的实例方法add_xx
        self.__c.add_xx(100)
