"""
    练习2：在控制台中循环录入学生信息（姓名，年龄，成绩，姓别），
    如果名称输入空字符，则停止录入
    将所有信息逐行打印出来
    用字典内嵌列表
{
    "张无忌":[28,100,"男"]
    "赵敏":[26,80,"女"]
}
"""

dict_students = {}
while True:
    name = input("请输入学生姓名：")
    if name == "":
        break
    age = int(input("请输入学生年龄："))
    score = int(input("请输入学生成绩："))
    sex = input("请输入学生性别：")
    dict_students[name] = [age, score, sex]
for k, v in dict_students.items():
    print(f"{k}今年{v[0]}岁，成绩是{v[1]},性别是{v[2]}")
