"""
    练习：猜数字游戏
    游戏运行产生一个1-100之间的随机数。
    让玩家重复猜测，直到才对为止。
    提示：大了
        小了
        猜对了
"""
# 随机数工具（在开头写一次）
import random

# 产生一个随机数
random_number = random.randint(1, 100)

count = 0
while True:
    count += 1
    guess_number = int(input("请输入一个1-100的数字："))
    if guess_number == random_number:
        print("猜对了！总共猜了%d次" % count)
        break
    elif guess_number > random_number:
        print("大了")
    else:
        print("小了")
