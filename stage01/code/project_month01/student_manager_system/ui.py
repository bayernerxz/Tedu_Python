# -*- coding:utf-8 -*-
"""
    界面代码
"""

from bll import StudentManagerController, StudentModel


class StudentManagerView:
    """
    学生管理器视图
    """

    def __init__(self):
        """
        初始化时，创建一个控制器的实例变量，避免main()中的循环每次都会创建一个实例变量
        """
        self.__manager = StudentManagerController()

    @staticmethod
    def __display_menu():
        """
        显示菜单信息
        """
        print("1. 添加学生信息")
        print("2. 显示学生信息")
        print("3. 删除学生信息")
        print("4. 修改学生信息")
        print("5. 按学生成绩低~高显示学生信息")

    def __select_menu(self):
        """
        选择一个选项
        :return: bool，如果不选返回一个False，让main()函数退出循环，否则返回True
        """
        option = input("请选择：")
        if option == "1":
            self.__input_students()
        elif option == "2":
            self.__output_students()
        elif option == "3":
            self.__remove_students()
        elif option == "4":
            self.__modify_student()
        elif option == "5":
            self.__output_students_by_score()
        elif option == "":
            return False
        else:
            print("输入错误，请输入1-5的整数选项：")
        return True

    def __input_students(self):
        """
        输入学生信息
        """
        name = input("请输入姓名：")
        age = self.__handle_error_input("请输入年龄：", 60, 3)
        score = self.__handle_error_input("请输入成绩：", 100)
        temp_stu = StudentModel(name, age, score)
        self.__manager.add_student(temp_stu)

    @staticmethod
    def __handle_error_input(prompt, max_value, min_value=0):
        """
            处理错误输入
        :param prompt:提示输入的信息
        :param max_value: 允许的最大值
        :param min_value: 允许的最小值，默认为0
        :return: 用户输入的值
        """
        while True:
            str_value = input(prompt)
            try:
                value = int(str_value)
            except ValueError:
                print(f"输入错误，请输入{min_value}-{max_value}的整数。")
                continue
            if min_value <= value <= max_value:
                return value
            else:
                print(f"输入错误，请输入{min_value}-{max_value}的整数。")

    def __output_students(self, ref_list=None):
        """
        输入学生信息
        """
        if ref_list:
            for item in ref_list:
                print(f"学号：{item.id} 姓名：{item.name} 年龄：{item.age} 成绩：{item.score}")
        else:
            for item in self.__manager.stu_list:
                print(f"学号：{item.id} 姓名：{item.name} 年龄：{item.age} 成绩：{item.score}")

    def __remove_students(self):
        """
        删除学生信息
        """
        self.__output_students()
        stu_id = self.__handle_error_input("请输入需要删除的学生学号：", int(self.__manager.stu_list[-1]),
                                           int(self.__manager.stu_list[1]))
        if StudentManagerController.remove_student(self.__manager, stu_id):
            print("删除成功，现在的学生名单如下：")
            self.__output_students()
        else:
            print("删除失败。")

    @staticmethod
    def __generate_dict(name, age, score):
        """
        生成并返回一个包含学生信息的字典,形如：{"name": "Jim", "age" = 28, "score" = 100}
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        :return: 返回dict
        """
        temp_dict = {}
        if name != "":
            temp_dict["name"] = name
        if age != "":
            temp_dict["age"] = age
        if score != "":
            temp_dict["score"] = score
        return temp_dict

    def __modify_student(self):
        """
        修改学生信息
        """
        self.__output_students()
        stu_id = self.__handle_error_input("请输入需要修改的学生学号：", len(self.__manager.stu_list), 1)
        name = input("请输入姓名：")
        age = self.__handle_error_input("请输入年龄：", 60, 3)
        score = self.__handle_error_input("请输入成绩：", 100)
        temp_dict = self.__generate_dict(name, age, score)
        stu = self.__manager.find_student(stu_id)
        self.__manager.update_student(stu, temp_dict)

    def __output_students_by_score(self):
        """
        按成绩由低到高输出学生信息
        """
        temp_list = self.__manager.order_by_score("ascending")
        self.__output_students(temp_list)

    def main(self):
        continue_process = True
        while continue_process:
            self.__display_menu()
            continue_process = self.__select_menu()
