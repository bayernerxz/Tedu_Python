# 练习:定义根据成绩计算等级的函数

def get_grade(score):
    """
    根据成绩计算等级
    :param score: 成绩，int
    :return: 等级，str
    """
    # if score > 100 or score < 0:
    #     return "输入有误"
    # elif 90 <= score:
    #     return "优秀"
    # elif 80 <= score:
    #     return "良好"
    # elif 60 <= score:
    #     return "及格"
    # else:
    #     return "不及格"

    if score > 100 or score < 0:
        return "输入有误"  # 因为return会直接退出函数，所以后面不需要elif，逻辑简洁
    if 90 <= score:
        return "优秀"
    if 80 <= score:
        return "良好"
    if 60 <= score:
        return "及格"
    return "不及格"


print(get_grade(59))
