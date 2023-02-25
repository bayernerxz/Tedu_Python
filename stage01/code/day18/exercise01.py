"""
    3．定义敌人类(姓名，攻击力，防御力，血量)
    创建敌人列表，使用list_helper实现下列功能.
        (1)查找姓名是"灭霸"的敌人
        (2)查找攻击力大于50的所有敌人
        (3)查找活的敌人数量

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

result = ListHelper.find_single(enemy_list, lambda element: element.name == "灭霸")
print(result)

generator_result = ListHelper.find_all(enemy_list, lambda element: element.attack > 50)
for item in generator_result:
    print(item)

# 生成器 --> 惰性操作
# 优势：节省内存
# 缺点：获取结果不灵活（不能使用索引/切片访问结果）
# 解决：惰性操作 --> 立即操作
list_result = list(generator_result)
for item in list_result[:2]:
    print(item)

result = ListHelper.find_quantity(enemy_list, lambda element: element.life > 0)
print(result)

re = ListHelper.is_exist(enemy_list, lambda element: element.name == "成昆")
print(re)
re = ListHelper.is_exist(enemy_list, lambda element: element.attack < 5 or element.defend < 10)
print(re)
