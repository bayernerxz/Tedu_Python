"""
    内置高阶函数
"""
from common.list_helper import *


class Enemy:
    def __init__(self, name, life, attack, defend):
        self.name = name
        self.life = life
        self.attack = attack
        self.defend = defend

    def __str__(self):
        return f"此敌人的姓名：{self.name},血量{self.life},攻击力{self.attack},防御力{self.defend}"


enemy_list = [Enemy("近战小兵", 100, 20, 10), Enemy("远程小兵", 80, 30, 5), Enemy("炮车兵", 600, 50, 15),
              Enemy("超级兵", 1000, 100, 50), Enemy("灭霸", 10000, 10000, 200), Enemy("死亡的近战小兵", 0, 20, 10),
              Enemy("残废的远程小兵", 0, 30, 5)]

# 1.filter：根据条件筛选可迭代对象中的元素，返回值为新可迭代对象。
# 需求：获取所有死人
for item in ListHelper.find_all(enemy_list, lambda item: item.life == 0):
    print(item)

re = filter(lambda item: item.life == 0, enemy_list)
for item in re:
    print(item)

# 2.map:通用的筛选方法
#       使用可迭代对象中的每个元素调用函数，将返回值作为新可迭代对象元素；返回值为新可迭代对象。
# 需求：获取所有敌人的姓名
for item in ListHelper.screen_to_generator(enemy_list, lambda item: item.name):
    print(item)

for item in map(lambda item: item.name, enemy_list):
    print(item)

# 3.max:获取最大值
# 需求：获取血量最大的敌人
print(ListHelper.get_max(enemy_list, lambda item: item.life))

print(max(enemy_list, key=lambda item: item.life))
# def max(*args, key=None):
# 命名关键字形参在传参时，必须把关键字加等号打出来

# 4.min:获取最小值
# 略

# 5.sorted:排序，返回值为排序结果

# 内部直接个性列表，使用时无需通过返回值获取数据
ListHelper.sort_ascending(enemy_list, lambda item: item.life)
for item in enemy_list:
    print(item)

# 内部返回新列表，使用时必须获取返回值
re = sorted(enemy_list, key=lambda item: item.life)
for item in re:
    print(item)

# 支持降序排列
re = sorted(enemy_list, key=lambda item: item.life,reverse=True)
for item in re:
    print(item)