"""
    练习1：
    在控制台中录入，西游记中你喜欢的人物。
    输入空字符串，打印所有（一行一个）人物。
"""

list_person = []
while True:
    string = input("请输入西游记中你喜欢的人物：")
    if string != "":
        list_person.append(string)
    else:
        break
for i in range(len(list_person)):
    print(list_person[i])
