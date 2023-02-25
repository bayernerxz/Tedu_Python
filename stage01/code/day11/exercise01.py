# 练习：定义敌人类（姓名，攻击力10-50，血量100-200）
#       创建一个敌人对象，可以修改数据，读取数据


class Enemy:
    def __init__(self, name, attack, hp):
        self.name = name
        self.set_attack(attack)
        self.set_hp(hp)

    def set_attack(self, value):
        if 10 <= value <= 50:
            self.__attack = value
        else:
            raise ValueError("攻击过低，请输入10至50的整数。")

    def get_attack(self):
        return self.__attack

    def set_hp(self, value):
        if 100 <= value <= 200:
            self.__hp = value
        else:
            raise ValueError("血量过低，请输入100至200的整数。")

    def get_hp(self):
        return self.__hp


e01 = Enemy("小兵", 10, 100)
print(e01.get_name(), e01.get_attack(), e01.get_hp())
