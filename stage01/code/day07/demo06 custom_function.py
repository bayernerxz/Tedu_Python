"""
    自定义函数
"""


# 定义（作功能）函数
def attack():
    """
    单次攻击
    """
    print("摆拳")
    print("直拳")
    print("肘击")
    print("临门一脚")


# 形式参数 parameter
def attack_repeat(count):
    """
    重复攻击
    :param count:攻击次数,int类型
    """
    for i in range(count):
        print("摆拳")
        print("直拳")
        print("肘击")
        print("临门一脚")


# 调用函数
attack()
# 。。。。。。
attack()
# 。。。。。
attack()
print("-"*20)

# 调用函数
# 实际参数 argument
attack_repeat(4)
