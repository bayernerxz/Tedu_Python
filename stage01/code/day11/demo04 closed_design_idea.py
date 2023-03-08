"""
    封闭设计思想
        需求：老张开车去东北

"""


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def move_to(self, str_position, vehicle):
        print(f"{self.name}{vehicle.run(str_position)}")


class Car:
    def run(self, str_position):
        """
            行驶
        :param str_position:目的地
        :return: 字符串，开车去目的地
        """
        return f"开车去{str_position}"


lz = Person("老张")
car = Car()

lz.move_to("东北", car)
