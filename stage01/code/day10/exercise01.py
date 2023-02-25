"""
# 练习：参照day06/exercise07.py
1. 创建学生类
    --数据：姓名，年龄，成绩，性别
    -- 行为：再控制台中打印个人信息的方法
2. 在控制台中循环录入学生信息，如果名称是空字符，退出录入
3. 在控制台中输出每个学生信息（调用打印学生类的打印方法）
4. 打印第一个学生信息
"""


class Student:
    def __init__(self, name, age, score, sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def output_info(self):
        print(f"{self.name}年龄是{self.age}，成绩是{self.score}，性别是{self.sex}。")


def input_info():
    name = input("请输入学生姓名：")
    if name == "":
        return "", "", "", ""
    age = int(input("请输入学生年龄："))
    score = int(input("请输入学生成绩："))
    sex = input("请输入学生性别：")
    return age, name, score, sex


def input_student_name():
    while True:
        age, name, score, sex = input_info()
        if name == "":
            break
        list_student.append(Student(name, age, score, sex))


list_student = []
input_student_name()
for item in list_student:
    item.output_info()
print("第一个录入的是", end="")
list_student[0].output_info()
