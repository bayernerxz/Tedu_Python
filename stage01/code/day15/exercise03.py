"""
    定义函数，在控制参中获取成绩的函数。
    要求：如果异常，继续获取成绩，直到得到正确的成绩。
        成绩必须在0-100之间，还继续输入。
"""


def get_score():
    while True:
        try:
            num_score = int(input("请输入成绩："))
        except:
            print("输入的不是整数。")
            continue
        if 0 <= num_score <= 100:
            return num_score
        else:
            print("超过范围。")


score = get_score()
print("成绩是%d" % score)
