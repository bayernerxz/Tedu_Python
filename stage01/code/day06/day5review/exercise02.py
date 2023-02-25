"""
彩票  双色球：
红球：6个，1-33之间的整数，不能重复
蓝球：1个，1-16之间的整数
1）随机产生一注彩票【6个红球1个蓝球】
2）在控制台中购买一注彩票
提示：
    "请输入第1个红球号码："
    "请输入第2个红球号码："
    "号码不在范围内"
    "号码已经重复"
    "请输入蓝球号码"
"""

import random


def rand_ball():
    redball_list = []
    blueball_list = []
    while len(redball_list) <= 6:
        temp_num = random.randint(1, 33)
        if temp_num not in redball_list:
            redball_list.append(temp_num)

    blueball_list.append(random.randint(1, 16))

    print(f"""此次机选的号码是:
    
红球：{redball_list[0]} {redball_list[1]} {redball_list[2]} {redball_list[3]} {redball_list[4]} {redball_list[5]}；

蓝球： {blueball_list[0]}
""")


def choose_ball():
    ticket_list = []
    while len(ticket_list) < 6:
        temp_num = int(input(f"请输入第{len(ticket_list) + 1}个红球号码："))
        if temp_num > 33 or temp_num < 1:
            print("号码不在范围内")
        elif temp_num in ticket_list:
            print("号码已经重复")
        else:
            ticket_list.append(temp_num)
    while len(ticket_list) < 7:
        temp_num = int(input("请输入蓝球号码："))
        if 16 >= temp_num >= 1:
            ticket_list.append(temp_num)
        else:
            print("号码不在范围内")

    print(f"""此次您选择的号码是:
    
红球：{ticket_list[0]} {ticket_list[1]} {ticket_list[2]} {ticket_list[3]} {ticket_list[4]} {ticket_list[5]}；

蓝球： {ticket_list[6]}
""")


if __name__ == "__main__":
    rand_ball()
    choose_ball()
