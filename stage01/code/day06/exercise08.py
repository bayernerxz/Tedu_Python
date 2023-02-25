"""
    需求：存储多个学生信息（姓名，年龄，成绩，性别）
    用字典内嵌列表
{
    "张无忌":[28,100,"男"]
    "赵敏":[26,80,"女"]
}
    用字典内嵌字典
{
    "张无忌":{"age":28,"score":100,"sex":"男"}
    "赵敏":{"age":25,"score":80,"sex":"女"}
}
    用列表内嵌字典
[
    {"name":"张无忌","age":28,"score":100,"sex":"男"}
    {"name":"赵敏","age":25,"score":80,"sex":"女"}
]
    选择策略：根据具体需求，结合优缺点，综合考虑（两害相权取其轻）
    字典：
        优点：
            根据键获取值，读取速度快；
            代码可读性相对列表更高（根据键获取与根据索引获取相比）；
        缺点：
            内存占用大；
            猎取值只能根据键，不灵活。
    列表：
        优点：
            根据索引、切片，获取元素更灵活；
            相比字典占内存更小。
        缺点：
            通过索引获取，如果信息较多，可主动性不高。

"""

# 练习：在控制台中录入多个人的多个喜好
# 例如：请输入姓名：
#       请输入第一个喜好：
#       请输入第二个喜好：
#       ……
#       请输入姓名：
#       输入空字符停止
#       最后在控制台打印所有人的所有喜好

person_hobby = []
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    person = [name]
    while True:
        hobby = input("请输入喜好：")
        if hobby == "":
            break
        person.append(hobby)
    person_hobby.append(person)

for person_count in range(len(person_hobby)):
    print("第%d个人的姓名是%s" % (person_count + 1, person_hobby[person_count][0]))  # 打印姓名
    for hobby_count in range(1, len(person_hobby[person_count])):
        print("他的第%d个兴趣是：%s" % (hobby_count, person_hobby[person_count][hobby_count]))
