# 练习：定义敌人类（姓名，攻击力10-50，血量100-200）
#       创建一个敌人对象，可以修改数据，读取数据
#       使用property()封装变量


class Enemy:
    def __init__(self, name, attack, hp):
        self.name = name
        self.attack = attack
        self.hp = hp

    def set_attack(self, value):
        if 10 <= value <= 50:
            self.__attack = value
        else:
            raise ValueError("攻击过低，请输入10至50的整数。")

    def get_attack(self):
        return self.__attack

    attack = property(get_attack, set_attack)

    def set_hp(self, value):
        if 100 <= value <= 200:
            self.__hp = value
        else:
            raise ValueError("血量过低，请输入100至200的整数。")

    def get_hp(self):
        return self.__hp

    hp = property(get_hp, set_hp)
    # 把get_hp改成None，就变为只可以写操作这个变量
    # hp = property(None, set_hp)
    # 把set_hp改成None，就变为只可以读操作这个变量
    # hp = property(get_hp, None)


e01 = Enemy("小兵", 10, 100)
print(e01.name, e01.attack, e01.hp)
