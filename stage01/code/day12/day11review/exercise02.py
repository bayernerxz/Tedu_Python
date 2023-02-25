"""
    请用面向对象的思想，描述以下场景：
        玩家（攻击力）攻击敌人（血量），敌人受伤(掉血)，还可能死亡（掉装备，加分）。
        敌人（攻击力）攻击玩家，玩家（血量）受伤后掉血/碎屏，还可能死亡（游戏结束）。
"""


class Character:
    def __init__(self, name, hp, atk, *equipment):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.equipment = equipment

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def equipment(self):
        return self.__equipment

    @equipment.setter
    def equipment(self, value):
        self.__equipment = value

    def attack(self, target):
        print(f"{self.name}攻击了{target.name}。")
        target.wound(self)
        if target.is_death():
            target.death()

    def is_death(self):
        if self.hp == 0:
            return True


class PlayerCharacter(Character):

    def wound(self, attacker):
        self.hp -= attacker.atk
        if self.hp < 0:
            self.hp = 0
        print(f"来自{attacker.name}的攻击造成了{attacker.atk}点伤害。\n{self.name}还剩下{self.hp}点血量。")
        Screen.break_screen()

    def death(self):
        if self.hp == 0:
            print("大侠请重新来过。")


class NonePlayerCharacter(Character):
    def wound(self, attacker):
        self.hp -= attacker.atk
        if self.hp < 0:
            self.hp = 0
        print(f"来自{attacker.name}的攻击造成了{attacker.atk}点伤害。\n{self.name}还剩下{self.hp}点血量。")

    def death(self):
        import random
        drop_index = random.randint(0, len(self.equipment) - 1)
        print(f"{self.name}已经死亡，掉落了{self.equipment[drop_index]}。")


class Screen:
    @staticmethod
    def break_screen():
        print("屏碎了！")


if __name__ == "__main__":
    zwj = PlayerCharacter("张无忌", 100, 10, "屠龙刀", "软猬甲", "蚕丝手套", "疾行靴")
    xb = NonePlayerCharacter("小兵", 10, 2, "砍刀", "锁子甲", "布鞋")
    zwj.attack(xb)
