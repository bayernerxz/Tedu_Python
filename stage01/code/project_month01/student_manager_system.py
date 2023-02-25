"""
    学生管理系统
    项目计划：
            1.完成数据模型类StudentModel
            2.创建逻辑控制类StudentManagerController
            3.完成数据：学生列表__stu_list
            4.行为：获取列表stu_list，
            5.添加学生方法 add_student
            6.根据编号删除学生remove_student
            7.根据编号修改学生update_student

"""


class StudentModel:
    """
        学生信息模型
    """

    def __init__(self, name="", age=0, score=0, id=0):
        """
        创建学生对象
        :param name:姓名，str类型。
        :param age:年龄，int类型
        :param score:成绩，float类型
        :param id:编号（该学生对象的唯一标识）
        """
        self.name = name
        self.age = age
        self.score = score
        self.id = id


class StudentManagerController:
    """
    学生管理控制器，负责业务逻辑处理
    """

    # 类变量，表示初始编号
    __init_id = 1000

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        """
        学生列表
        :return:存储学生对象的列表
        """
        return self.__stu_list

    def add_student(self, stu_info):
        """
        添加一个新学生
        :param stu_info:没有编号的学生信息
        """
        stu_info.id = self.__generate_id()
        self.__stu_list.append(stu_info)

    @staticmethod
    def __generate_id():
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def remove_student(self, id):
        """
        根据编号移除学生
        :param id: 编号，int类型
        :return: bool，True表示删除成功，False表示删除失败
        """
        for item in self.stu_list:
            if item.id == id:
                self.stu_list.remove(item)
                return True  # 表示移除成功
        return False  # 表示移除失败

    def update_student(self, stu_info):
        """
        修改学生信息
        :param stu_info: 需要修改后的学生对象
        :return: bool，True表示修改成功，False表示修改失败
        """
        # 根据stu_info.id修改其他信息
        for item in self.stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False


class StudentManagerView:
    """
    学生管理器视图
    """

    @staticmethod
    def __display_menu():
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩升序显示学生")

    @staticmethod
    def __select_menu():
        item = input("请输入：")
        if item == "1":
            pass
        elif item == "2":
            pass
        elif item == "3":
            pass
        elif item == "4":
            pass
        elif item == "5":
            pass

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()