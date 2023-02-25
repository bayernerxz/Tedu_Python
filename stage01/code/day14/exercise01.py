# 练习：创建Enemy类对象，将对象打印在控制台中（格式自定义）
#       克隆Enemy类对象，体会克隆对象变量的改变不影响原对象

class Enemy:
    def __init__(self, name, attack, hp, defense):
        self.name = name
        self.attack = attack
        self.hp = hp
        self.defense = defense

    def __str__(self):
        return f"敌人是：{self.name},攻击力{self.attack},防御力{self.defense},生命值{self.hp}"

    def __repr__(self):
        return f"Enemy('{self.name}',{self.attack},{self.hp},{self.defense})"


e01 = Enemy("小兵", 10, 50, 0)
print(e01)
# print(repr(e01))
e02 = eval(repr(e01))
e02.hp = 500
print(e01, e02, sep="\n")
