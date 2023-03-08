"""
bool
运算符
    比较运算符 > < >= <= 等于== 不等于!=
            结果是：bool类型
    逻辑运算符：判断两个bool值关系
            与   或   非
"""
# 1.bool类型
# 取值：（真，对的）True （假，错的）False
# 命题：带有判断性的陈述句。
# 例如：我是个男人。
# 1>2 --> False
print(1 > 2)

# 2.逻辑运算符
# -- 与：一假俱假，表示并且（都得满足）的关系
print(True and True)  # True 都得满足条件，结论采满足条件
print(False and True)  # False
print(True and False)  # False
print(False and False)  # False

# -- 或：一真俱真，表示或者（一个满足就行）的关系
print(True or True)  # True 都得满足条件，结论采满足条件
print(False or True)  # True
print(True or False)  # True
print(False or False)  # False

# -- 非：取反
print(not True)
