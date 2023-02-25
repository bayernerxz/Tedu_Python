"""
    测试 common模块中list_helper.py
"""

from common.list_helper import *


class SkillData:
    def __init__(self, id, name, atk_ratio, duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

    def __str__(self):
        return f"技能数据是：{self.id},{self.name},{self.atk_ratio},{self.duration}"


list_skill = [
    SkillData(101, "乾坤大挪移", 5, 10),
    SkillData(102, "降龙十八掌", 8, 5),
    SkillData(103, "葵花宝典", 10, 2),
]

# 练习：在list_helper.py中，定义通用的查找满足条件的单个对象。
# 案例：查找名称是“葵花宝典”的技能
#       查找持续时间大于0的技能。
# 建议：
# 1.先将所有功能实现
# 2.封装变化（将变化点单独定义为函数）
#   定义不变的函数
# 3.将不变的函数转移到list_helper.py中
# 4.在当前模块测试

# def condition1(item):
#     return item.name == "葵花宝典"
#
#
# def condition2(item):
#     return item.duration >= 0


# 练习1：在exercise06.py中，使用def定义的函数，改为使用lambda定义。
re1 = ListHelper.find_single(list_skill, lambda item: item.name == "葵花宝典")
print(re1)

re2 = ListHelper.find_single(list_skill, lambda item: item.duration >= 0)
print(re2)

print("-" * 20)
# 需求1：计算技能列表中技能名称大于4个字的技能数量。
# 需求2：计算技能列表中技能持续时间小于等于5的技能数量。
# 实现每个需求/单独封装变化/定义不变的函数（“继承”/“多态”）
# 将不变的函数提取到list_helper.py中

re3 = ListHelper.find_quantity(list_skill, lambda element: len(element.name) > 4)
re4 = ListHelper.find_quantity(list_skill, lambda element: element.duration <= 5)
print(re3, re4)
