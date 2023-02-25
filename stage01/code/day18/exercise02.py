"""
    # 练习1：
    在list_helper.py中增加通用的求和方法。
    案例1：计算敌人列表中所有敌人的总血量。
    案例2：计算敌人列表中所有敌人的总攻击力。
    案例3：计算敌人列表中所有敌人的总防御力。
    步骤：
    实现具体功能/提取变化/提取不变/组合

    # 练习2：
    在list_helper.py中增加通用的筛选方法。
    案例1：获取敌人列表中所有敌人的名称的列表。
    案例2：计算敌人列表中所有敌人的攻击力。
    案例3：计算敌人列表中所有敌人的姓名和血量。

    # 练习3：
    在list_helper.py中增加通用的获取最大值方法。
    案例1：获取敌人列表中攻击力最大的敌人。
    案例2：获取敌人列表中防御力最大的敌人。
    案例3：获取敌人列表中血量最高的敌人。

    # 练习4：
    在list_helper.py中增加通用的升序排列方法。
    案例1：获取敌人列表按照攻击力进行升序排列。
    案例2：获取敌人列表按照防御力进行升序排列。
    案例3：获取敌人列表按照血量进行升序排列。

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

# 案例1：计算敌人列表中所有敌人的总血量。
re = ListHelper.sum_property(enemy_list, lambda e: e.life)
print(re)

# 案例2：计算敌人列表中所有敌人的总攻击力。
re = ListHelper.sum_property(enemy_list, lambda e: e.attack)
print(re)

# 案例3：计算敌人列表中所有敌人的总防御力。
re = ListHelper.sum_property(enemy_list, lambda e: e.defend)
print(re)

# 案例1：获取敌人列表中所有敌人的名称的列表。
re = ListHelper.screen_to_list(enemy_list, lambda e: e.name)
print(re)
# 案例2：计算敌人列表中所有敌人的攻击力。
re = ListHelper.screen_to_list(enemy_list, lambda e: e.attack)
print(re)
# 案例3：计算敌人列表中所有敌人的姓名和血量。
re = ListHelper.screen_to_generator(enemy_list, lambda e: (e.name, e.life))
for i in re:
    print(i)

# 案例1：获取敌人列表中攻击力最大的敌人。
re1 = ListHelper.get_max(enemy_list, lambda e: e.attack)
# 案例2：获取敌人列表中防御力最大的敌人。
re2 = ListHelper.get_max(enemy_list, lambda e: e.defend)
# 案例3：获取敌人列表中血量最高的敌人。
re3 = ListHelper.get_max(enemy_list, lambda e: e.life)

print(re1, re2, re3, "\n", "-" * 20)

# 案例1：获取敌人列表按照攻击力进行升序排列。
ListHelper.sort_ascending(enemy_list, lambda e: e.attack)
print(enemy_list)
# 案例2：获取敌人列表按照防御力进行升序排列。
re2 = ListHelper.sort_ascending(enemy_list, lambda e: e.defend)
print(enemy_list)
# 案例3：获取敌人列表按照血量进行升序排列。
re3 = ListHelper.sort_ascending(enemy_list, lambda e: e.life)
print(enemy_list)

# ListHelper.delete_element(enemy_list, lambda e: e.name == "灭霸")
# re = ListHelper.screen_to_list(enemy_list, lambda e: e.name)
# print(re)