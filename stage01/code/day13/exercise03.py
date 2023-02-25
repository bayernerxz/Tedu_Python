"""
    手雷炸了，可能伤害敌人/玩家的生命。
            还可能伤害未知事物（鸭子，房子。。。）
    要求：增加了新事物，不影响手雷。
    体会：继承的作用
        金矿的体现
            设计原则
            单一职责
            依赖倒置
    画出设计图
"""


class Damageable:
    def injure(self, damage):
        pass


class Grenade:
    def explode(self, victim, damage):
        victim.injure(damage)


class Enemy(Damageable):
    def injure(self, damage):
        print("受到了%d点伤害。")
        print("头上跳字")


class Player(Damageable):
    def injure(self, damage):
        print("受到了%d点伤害。")
        print("屏碎了！")
