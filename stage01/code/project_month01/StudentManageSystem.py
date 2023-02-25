"""
    学生管理系统
    项目计划：
        1.完成数据模型类StudentModel
        2.创建逻辑控制类StudentManagerControl
        3.完成数据：学生列表__stu_list
        4.行为：获取列表 stu_list,
        5.添加学生方法 add_student
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
        按成绩排序
        :param order: 只能是ascending或descending
        """
        if order == "ascending":
            self.__ascending()
        if order == "descending":
            self.__descending()

    def __descending(self):
        """
        降序排列
        :return:
        """
        for i in range(len(self.stu_list) - 1):
            for j in range(i + 1, len(self.stu_list)):
                if self.stu_list[i].score < self.stu_list[j].score:
                    self.stu_list[i], self.stu_list[j] = \
                        self.stu_list[j], self.stu_list[i]

    def __ascending(self):
        """
        升序排列
        :return:
        """
        for i in range(len(self.stu_list) - 1):
            for j in range(i + 1, len(self.stu_list)):
                if self.stu_list[i].score > self.stu_list[j].score:
                    self.stu_list[i], self.stu_list[j] = \
                        self.stu_list[j], self.stu_list[i]

    def find_student(self, stu_id):
        """
        按学号查找__stu_list中的学生对象，
        :param stu_id:学号，int类型
        :return: 返回一个学生对象
        """
        for item in self.__stu_list:
            if item.id == stu_id:
                return item


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
        age = int(input("请输入年龄："))
        score = int(input("请输入成绩："))
        temp_stu = StudentModel(name, age, score)
        self.__manager.add_student(temp_stu)

    def __output_students(self):
        """
        输入学生信息
        """
        for item in self.__manager.stu_list:
            print(f"学号：{item.id} 姓名：{item.name} 年龄：{item.age} 成绩：{item.score}")

    def __remove_students(self):
        """
        删除学生信息
        """
        stu_id = int(input("清输入需要删除学生的学号："))
        if StudentManagerController.remove_student(self.__manager, stu_id):
            print("删除成功，现在的学生名单如下：")
            self.__output_students()
        else:
            print("删除失败")

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
            temp_dict["age"] = int(age)
        if score != "":
            temp_dict["score"] = int(score)
        return temp_dict

    def __modify_student(self):
        """
        修改学生信息
        """
        self.__output_students()
        stu_id = int(input("请输入需要修改的学生学号："))
        name = input("请输入姓名：")
        age = input("请输入年龄：")
        score = input("请输入成绩：")
        temp_dict = self.__generate_dict(name, age, score)
        stu = self.__manager.find_student(stu_id)
        self.__manager.update_student(stu, temp_dict)

    def __output_students_by_score(self):
        """
        按成绩由低到高输出学生信息
        """
        self.__manager.order_by_score("ascending")
        self.__output_students()

    def main(self):
        continue_process = True
        while continue_process:
            self.__display_menu()
            continue_process = self.__select_menu()


# 测试代码
if __name__ == "__main__":
    view = StudentManagerView()
    view.main()
