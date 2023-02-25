# -*- coding:utf-8 -*-
"""
    定义数据模型
"""


class StudentModel:
    """
    学生模型
    """

    def __init__(self, name="", age=0, score=0, stu_id=0):
        """
        创建学生对象
        :param name: 姓名，str类型
        :param age: 年龄，int类型
        :param score: 成绩，成绩类型
        :param stu_id:编号，该学生对象的唯一标识
        """
        self.name = name
        self.age = age
        self.score = score
        self.id = stu_id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value
