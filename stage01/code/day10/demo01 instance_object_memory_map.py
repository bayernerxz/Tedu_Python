"""
    实例对象内存图
    exercise01.py
"""

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
    Student("苏大强", 68, 62, "男")
]

s01 = list01[0]
s01.name = "小赵"
s01.score = 98
print(list01[0].name, list01[0].score)
print(list01[1].name, list01[1].score)

list01[0].output_info()  # 小赵年龄是28，成绩是98，性别是女。
list01[1].output_info()  # 苏大强年龄是68，成绩是62，性别是男。

