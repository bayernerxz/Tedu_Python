"""
    猜数字2.0：
        最多猜3次，如果猜对了提示”猜对了，总共踩了？次“
        如果超过次数，提示”游戏结束“
"""
# 随机数工具（在开头写一次）
import random

# 产生一个随机数
random_number = random.randint(1, 100)

count = 0
while count < 3:
    # 三次以内
    count += 1
    guess_number = int(input("请输入一个1-100的数字："))
    if guess_number == random_number:
        print("猜对了！总共猜了%d次" % count)
        break  # 退出循环体，不会执行else
    elif guess_number > random_number:
        print("大了")
    else:
        print("小了")
else:  # while的条件不满足
    # 三次意外
    print("游戏失败！")
