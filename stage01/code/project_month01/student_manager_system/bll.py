# -*- coding:utf-8 -*-

"""
    业务逻辑处理
"""

from model import StudentModel


class StudentManagerController:
    """
    学生管理控制器，负责业务逻辑处理。
    """

    # 类变量，表示初始编号
    __init_id: int = 0

    def __init__(self):
        """
        __stu_list，存放学生对象列表
        """
        self.__stu_list = []

    @property
    def stu_list(self):
        """
        学生列表
        :return:存储学生对象的列表
        """
        return self.__stu_list

    # 这样写不如下面，因为没有作到一个方法只作一件事
    # def add_student(self, name, age, score):
    #     self.__stu_list.append(StudentModel(self.id, name, age, score))
    #     self.id += 1

    def add_student(self, stu_info):
        """
        增加一个新学生
        :param stu_info:没有编号的学生信息
        :return:
        """
        # 可以通过对象.类变量名，来访问类变量，等同于类名.类变量名
        stu_info.id = self.__generate_id()
        self.stu_list.append(stu_info)

    def __generate_id(self):
        """
        生成学生编号
        :return: 返回处理过的学生编号
        """
        self.__init_id += 1
        return self.__init_id

    def remove_student(self, stu_id):
        """
        根据编号移除学生信息
        :param stu_id:需要删除的学生编号
        :return:bool，True表示移除成功，False表示移除失败
        """
        for item in self.__stu_list:
            if item.id == stu_id:
                self.stu_list.remove(item)
                return True  # 表示移除成功
        return False  # 表示移除失败

    def update_student(self, stu, updated_info):
        """
        更新学生信息
        :param stu:需要更数据的学生信息
        :param updated_info: 需要更新数据，dict类型，形如｛｝
        :return:
        """
        for i in range(len(self.__stu_list) - 1, -1, -1):
            if self.__stu_list[i] == stu:
                # 把self.__stu_list中相应位置的学生对象替换为更新过的
                self.__stu_list[i] = self.__update_student_info(i, updated_info)

    def __update_student_info(self, i, updated_info):
        """
        更新数据
        :param i:self.stu_list中的索引号，int类型
        :param updated_info: 需要更新数据形成的字典，dict类型
        :return: 一个更新过的学生对象
        """
        temp_dict = {"name": self.stu_list[i].name, "age": self.stu_list[i].age, "score": self.stu_list[i].score,
                     "stu_id": self.stu_list[i].id}
        for k, v in updated_info.items():
            temp_dict[k] = v
        return StudentModel(**temp_dict)

    def order_by_score(self, order="ascending"):
        """
        按成绩排序，不改变当前类的__stu_list
        :param order: 只能是ascending或descending
        :return:排序后的列表
        """
        if order == "ascending":
            return self.__ascending()
        if order == "descending":
            return self.__descending()

    def __descending(self):
        """
        降序排列
        :return:排序后的列表
        """
        temp_list = []
        for i in range(len(self.stu_list)):
            temp_list.append(self.stu_list[i])

        for i in range(len(temp_list) - 1):
            for j in range(i + 1, len(temp_list)):
                if temp_list[i].score < temp_list[j].score:
                    temp_list[i], temp_list[j] = \
                        temp_list[j], temp_list[i]
        return temp_list

    def __ascending(self):
        """
        升序排列
        :return:排序后的列表
        """
        temp_list = []
        for i in range(len(self.stu_list)):
            temp_list.append(self.stu_list[i])

        for i in range(len(temp_list) - 1):
            for j in range(i + 1, len(temp_list)):
                if temp_list[i].score > temp_list[j].score:
                    temp_list[i], temp_list[j] = \
                        temp_list[j], temp_list[i]
        return temp_list

    def find_student(self, stu_id):
        """
        按学号查找__stu_list中的学生对象，
        :param stu_id:学号，int类型
        :return: 返回一个学生对象
        """
        for item in self.__stu_list:
            if item.id == stu_id:
                return item
