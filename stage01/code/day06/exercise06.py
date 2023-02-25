"""
    练习2：在控制台中循环录入学生信息（姓名，年龄，成绩，姓别），
    如果名称输入空字符，则停止录入
    将所有信息逐行打印出来
    用字典内嵌字典
{
    "张无忌":{"age":28,"score":100,"sex":"男"}
    "赵敏":{"age":25,"score":80,"sex":"女"}
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

    dict_students[name] = {"age": age, "score": score, "sex": sex}

for k, v in dict_students.items():
    print("%s年龄是%d，成绩是%d，性别是%s。" % (k, v["age"], v["score"], v["sex"]))
    print(f"{k}年龄是{v['age']}，成绩是{v['score']}，性别是{v['sex']}。")
