"""
    内置高阶函数
    练习：
    1. ([1,1,1],[2,2],[3,3,3,3])
        获取元组中，长度最大的列表.
    2．根据敌人列表﹐获取所有敌人的姓名与血量与攻击力.
    3.在敌人列表中﹐获取攻击力大于100的所有活人.
    4．根据防御力对敌人列表进行降序排列.


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

tuple01 = ([1, 1, 1], [2, 2], [3, 3, 3, 3])

print(max(tuple01, key=lambda element: len(element)))

re = map(lambda element: (element.name, element.life, element.attack), enemy_list)
for item in re:
    print(item)

re = filter(lambda element: element.life > 0 and element.attack > 100, enemy_list)
for item in re:
    print(item)

re = sorted(enemy_list, key=lambda element: element.defend, reverse=True)
for item in re:
    print(item)
