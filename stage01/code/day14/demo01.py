"""
    内置可重写函数
"""


class StudentModel:
    def __init__(self, name="", age=0, score=0, stu_id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = stu_id

    # 对象--> 字符串（随意格式）
    def __str__(self):
        return f"姓名：{self.name}，学号：{self.id}，年龄：{self.age}，成绩：{self.id}"

    # 对象--> 字符串（解释器可识别，有格式的，符合python解释器语法）
    def __repr__(self):
        return 'StudentModel("%s", %d, %d, %d)' % (self.name, self.age, self.score, self.id)


s01 = StudentModel("无忌", 27, 100, 101)
str01 = str(s01)

print(str01)

print(s01)

str02 = repr(s01)
print(str02)

re = eval("1+2*5")
# exec eval可以根据字符串执行python代码
print(re)

# 克隆对象
# repr返回python格式的字符串（创建对象）
# eval根据字符串执行代码
s02 = eval(repr(s01))
s02.name = "老张"
print(s01, s02)
