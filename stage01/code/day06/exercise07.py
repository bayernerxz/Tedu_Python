"""
    练习2：在控制台中循环录入学生信息（姓名，年龄，成绩，姓别），
    如果名称输入空字符，则停止录入
    将最后一个信息打印出来
    用列表内嵌字典
[
    {"name":"张无忌","age":28,"score":100,"sex":"男"}
    {"name":"赵敏","age":25,"score":80,"sex":"女"}
]
"""
list_students = []
while True:
    name = input("请输入学生姓名：")
    if name == "":
        break
    age = int(input("请输入学生年龄："))
    score = int(input("请输入学生成绩："))
    sex = input("请输入学生性别：")
    dict_info = {"name": name, "age": age, "score": score, "sex": sex}
    list_students.append(dict_info)

info = list_students[-1]
print(f"{info['name']}年龄是{info['age']}，成绩是{info['score']}，性别是{info['sex']}。")
