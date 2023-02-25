"""
    请用面向对象思想﹐描逑以下场景︰
    张无忌教赵敏九阳神功
    赵敏教张无忌化妆
    张无忌上班挣了10000
    赵敏上班挣了6000
"""


class Person:
    def __init__(self, name, money, salary, *skills):
        self.name = name
        self.money = money
        self.salary = salary
        self.skills = skills

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    @property
    def skills(self):
        return self.__skills

    @skills.setter
    def skills(self, value):
        self.__skills = value

    def teach(self, student, skill):
        if skill in self.__skills:
            print(f"{self.name}教{student.name}{skill}")

    def make_money(self, work):
        self.money += self.salary
        print(f"{self.name}{work.name}挣了{self.salary}")


class Work:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


zwj = Person("张无忌", 5000, 10000, "太极拳", "九阳神功")
zm = Person("赵敏", 50000, 6000, "化妆")

normal_work = Work("上班")

zwj.teach(zm, "九阳神功")
zm.teach(zwj, "化妆")

zwj.make_money(normal_work)
zm.make_money(normal_work)
