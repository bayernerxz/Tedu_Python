class Student:
    def __init__(self, name, age, score, sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def output_info(self):
        print(f"{self.name}年龄是{self.age}，成绩是{self.score}，性别是{self.sex}。")


list01 = [
    Student("赵敏", 28, 100, "女"),
    Student("苏大强", 68, 62, "男"),
    Student("明玉", 30, 95, "女"),
    Student("无忌", 28, 100, "男"),
    Student("张三丰", 105, 96, "男"),
]


# 练习1：定义函数，在list01中查找name是"苏大强"的对象返回。
# 将名称与年龄打印在控制台中。
def search_student():
    temp_name = input("请输入需要查找的名字：")
    for item in list01:
        if item.name == temp_name:
            print("%s的成绩是%d" % (item.name, item.score))
            return item
    # 如果没找到，则返回空。而函数默认返回值就是空，所以可以不写
    # return None


# search_student()


# 练习2：定义函数，在list01中查找所有女同学。
# 将名称与年龄打印在控制台中。

def search_by_sex():
    tmp_list = []
    for item in list01:
        if item.sex == "女":
            tmp_list.append(item)
    return tmp_list


# re = search_by_sex()
# for item in re:
#     item.output_info()


# 练习3：定义函数，在list01中查找年龄 >=30的学生数量。

def find_score_more_than_30():
    i = 0
    for item in list01:
        if item.age >= 30:
            i += 1
    return i


# print(find_score_more_than_30())

# 练习4：定义函数，在list01中将所有学生的成绩归零。
def zero_score():
    for stu in list01:
        stu.score = 0


# zero_score()
# for item in list01:
#     item.output_info()

# 练习5：定义函数，获取list01中所有学生的名字。

def get_name():
    tmp_list = []
    for item in list01:
        tmp_list.append(item.name)
    return tmp_list


# print(get_name())

# 练习6：定义函数，在list01中查找年龄最大的学生对象。

def search_by_max_age():
    max_age_stu=list01[0]
    for item in list01:
        if item.age >= max_age_stu.age:
            max_age_stu = item
    return item


search_by_max_age().output_info()
