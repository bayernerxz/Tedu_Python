"""
4．在list_helper中增加判断是否存在某个对象的方法.返回值:true/false
    案例1:判断敌人列表中是否存在"成昆"
    案例2:判断敌人列表中是否有攻击力小于5或者防御力小于10的敌人.步骤:
    实现每个需求/单独封装变化/定义不变的函数("继承"/"多态")
    将不变的函数提取到list helper.py中
    体会∶函数式编程的思想(封装﹐继承﹐多态")
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


# 创建敌人列表（至少5个元素），并画出内存图。
enemy_list = [Enemy("近战小兵", 100, 20, 10), Enemy("远程小兵", 80, 30, 5), Enemy("炮车兵", 600, 50, 15),
              Enemy("超级兵", 1000, 100, 50), Enemy("灭霸", 10000, 10000, 200), Enemy("死亡的近战小兵", 0, 20, 10),
              Enemy("残废的远程小兵", 0, 30, 5)]

