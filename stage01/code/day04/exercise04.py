# 练习：重复根据成绩判断等级，如果录入空字符串则退出程序。
# 如果成绩录入错误次数达到3，则退出成绩并提示”成绩错误过多“

count = 0
while count < 3:
    string_input = input("请输入成绩：")
    if string_input == "":
        print("录入为空")
        break
    score = int(string_input)
    if 90 <= score <= 100:
        print("优秀")
    elif score >= 75:
        print("良好")
    elif score >= 60:
        print("及格")
    elif score >= 0:
        print("不及格")
    else:
        print("输入有误！")
        count += 1
else:
    print("成绩错误过多！")
