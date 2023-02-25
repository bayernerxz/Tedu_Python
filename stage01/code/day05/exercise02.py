"""
    练习2：
    在控制台中录入，所有学生成绩。
    输入空字符串，打印所有（一行一个）成绩。
    打印最高分，打印最低分，打印平均分
"""

list_score = []
while True:
    string = input("请输入学生成绩：")
    if string != "":
        list_score.append(int(string))
    else:
        break

for i in range(len(list_score)):
    print(list_score[i])

print(f"最高分是：{max(list_score)}，最低分是：{min(list_score)}，平均分是：{sum(list_score) / len(list_score):0.2f}")
