"""
练习3：
在控制台中录入，所有学生姓名。
如果姓名重复，则提示“姓名已经存在”，不添加到列表中。
如果录入空字符串，则倒序打印所有学生。
"""

list_name = []
while True:
    string = input("请输入学生姓名：")
    if string == "":
        break
    if string not in list_name:
        list_name.append(string)
    else:
        print("姓名已经存在")

for i in range(-1, -len(list_name)-1, -1):
    print(list_name[i])
