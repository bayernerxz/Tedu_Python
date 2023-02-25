"""
    在控制台中录入一个成绩，
    判断成绩（优秀/良好/及格/不及格/输入有误）
"""

score = int(input("请输入成绩："))

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
