# 练习：员工管理器记录多个员工
#       迭代员工管理器对象
class Employee:
    pass


class EmployeeManager:
    """
        员工管理器，可迭代对象
    """

    def __init__(self):
        self.__employees = []

    def add_member(self, member):
        self.__employees.append(member)

    def __iter__(self):
        return EmployeeIterator(self.__employees)


class EmployeeIterator:
    def __init__(self, employees):
        self.__employees = employees
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__employees) - 1:
            raise StopIteration
        temp = self.__employees[self.__index]
        self.__index += 1
        return temp


m01 = EmployeeManager()
m01.add_member(Employee())
m01.add_member(Employee())
m01.add_member(Employee())
m01.add_member(Employee())

for item in m01:
    print(item)
