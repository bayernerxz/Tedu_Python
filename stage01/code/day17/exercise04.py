"""
    参照day10/exercise02.py，完成下列练习
"""


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


# 练习1:获取攻击比例大于6的所有技能
# 要求:使用生成器函数/生成器表达式完成

def find01():
    for item in list_skill:
        if item.atk_ratio > 6:
            yield item


re01 = find01()
for item in re01:
    print(item)

re02 = (item for item in list_skill if item.atk_ratio > 6)
for item in re02:
    print(item)

print("-" * 20)


# 练习2:获取持续时间在4--11之间的所有技能
def find02():
    for item in list_skill:
        if 4 <= item.duration <= 11:
            yield item


for item in find02():
    print(item)

re = (item for item in list_skill if 4 <= item.duration <= 11)
for item in re:
    print(item)

print("-" * 20)


# 练习3:获取技能编号是102的技能
def find03():
    for item in list_skill:
        if item.id == 102:
            return item

# 明显只有一个结果的查找就可以用return
re = find03()
print(re.id)

print("-" * 20)


# 练习4:获取技能名称大于4个字并且持续时间小于6的所有技能
def find04():
    for item in list_skill:
        if len(item.name) > 4 and item.duration < 6:
            yield item


for item in find04():
    print(item)

# 代码太长，可读性不高，不建议写成生成器表达式
# re = (item for item in list_skill if len(item.name) > 4 and item.duration < 6)
# for item in re:
#     print(item)
