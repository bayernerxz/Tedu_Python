"""
    定义员工管理器
        1.管理所有员工
        2.计算所有员工工资

    员工：
        程序员：底薪+项目分红
        销售：底薪+销售额 * 0.05
        软件测试：底薪+BUG数*5
        ...

    要求：增加新岗位，员工管理器不变。

"""


class StaffManager:
    """
    员工管理器类，可以增员工，计算总工资
    """

    def __init__(self):
        self.__staff_list = []

    @property
    def staff_list(self):
        return self.__staff_list

    def add_staff(self, *staff):
        """
        添加多个员工
        :param staff:员工对象
        """
        for item in staff:
            if isinstance(item, Staff):
                self.__staff_list.append(item)
                print(f"{item.name}已经添加到员工列表。")

    def calc_all_staff_salary(self):
        total_salary = 0
        for staff in self.__staff_list:
            total_salary += staff.get_salary()
        return total_salary


class Staff:
    __stuff_id = 0

    def __init__(self, name, base_salary):
        Staff.__stuff_id += 1
        self.__id = Staff.__stuff_id
        self.name = name
        self.base_salary = base_salary

    @property
    def id(self):
        return self.__id

    def get_salary(self):
        return self.base_salary


class Programmer(Staff):
    def __init__(self, name, base_salary, project_dividend):
        super().__init__(name, base_salary)
        self.project_dividend = project_dividend

    def get_salary(self):
        # 使用扩展重写（里氏替换法则）
        return super().get_salary() + self.project_dividend


class Salesmen(Staff):
    def __init__(self, name, base_salary, sales_volume):
        super().__init__(name, base_salary)
        self.sales_volume = sales_volume

    def get_salary(self):
        return super().get_salary() + 0.05 * self.sales_volume


class Tester(Staff):
    def __init__(self, name, base_salary, bug_num):
        super().__init__(name, base_salary)
        self.bug_num = bug_num

    def get_salary(self):
        return super().get_salary() + 5 * self.bug_num


if __name__ == "__main__":
    manager = StaffManager()
    manager.add_staff(Programmer("张三", 5000, 15000), Salesmen("李四", 3000, 100000))
    print(manager.staff_list[0].id, manager.staff_list[0].name)
    print(manager.calc_all_staff_salary())
