"""
4. 定义敌人类
    ——数据：姓名，血量，基础攻击力，防御力
    ——行为：打印个人信息

    创建敌人列表（至少5个元素），并画出内存图。
    查找姓名是灭霸的敌人对象
    查找所有死亡的敌人（血量为0）
    计算所有敌人的平均攻击力
    删除防御力小于10的敌人
    将所有敌人攻击力增加50
"""


class Enemy:
    def __init__(self, name, life, attack, defend):
        self.name = name
        self.life = life
        self.attack = attack
        self.defend = defend

    def print_name(self):
        print(self.name)


# 创建敌人列表（至少5个元素），并画出内存图。
enemy_list = [Enemy("近战小兵", 100, 20, 10), Enemy("远程小兵", 80, 30, 5), Enemy("炮车兵", 600, 50, 15),
              Enemy("超级兵", 1000, 100, 50), Enemy("灭霸", 10000, 10000, 200), Enemy("死亡的近战小兵", 0, 20, 10),
              Enemy("残废的远程小兵", 0, 30, 5)]


# 查找姓名是灭霸的敌人对象
def find01(list_ref):
    for item in list_ref:
        if item.name == "灭霸":
            print(item.name, item.life, item.attack, item.defend)
    return item


# 查找所有死亡的敌人（血量为0）
def find02(list_ref):
    result = []
    for item in list_ref:
        if item.life == 0:
            print(item.name, item.life, item.attack, item.defend)
            result.append(item)
    return result


# 计算所有敌人的平均攻击力
def average_attack(list_ref):
    total_attack = 0
    count = 0
    for item in list_ref:
        total_attack += item.attack
        count += 1
    return total_attack / count


# 删除防御力小于10的敌人
def del01(list_ref):
    print(len(list_ref))
    for i in range(len(list_ref) - 1, -1, -1):
        if list_ref[i].defend < 10:
            del list_ref[i]
    return list_ref


# 将所有敌人攻击力增加50
def add_attack(list_ref):
    for item in list_ref:
        item.attack += 50
        print(item.name, item.life, item.attack, item.defend)
    return list_ref
