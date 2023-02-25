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

print(ListHelper.get_min(enemy_list, lambda item: item.life))

ListHelper.sort_descending(enemy_list, lambda item: item.attack)
for item in enemy_list:
    print(item)

ListHelper.delete_element(enemy_list, lambda item: item.life == 0)
for item in enemy_list:
    print(item)
