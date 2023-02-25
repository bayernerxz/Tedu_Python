"""

"""

list01 = [43, 4, 5, 5, 6, 7, 87]


# 需求1:在列表中查找所有偶数
# 需求2:在列表中查找所有大于10的数
# 需求3:在列表中查找所有范围在10--50之间的数

# 1．使用生成器函数实现以上3个需求
# 2．体会函数式编程的"封装"
#           将三个函数变化点提取到另外三个函数中.
#           将共性提取到另外一个函数中
# 3．体会函数式编程的"继承"与"多态"
#       使用变量隔离变化点，在共性函数中调用变量.
# 4．测试(执行上逑功能)

def find01():
    for i in list01:
        if i % 2 == 0:
            yield i


def find02():
    for i in list01:
        if i > 10:
            yield i


def find03():
    for i in list01:
        if 10 < i < 50:
            yield i


# 封装
def condition01(i):
    return i % 2 == 0


def condition02(i):
    return i > 10


def condition03(i):
    return 10 < i < 50


# "继承"
def find(func_condition):
    for i in list01:
        # 多态
        # 调用：具体条件的抽象
        # 执行：具体条件的函数
        if func_condition(i):
            yield i


# 测试
for i in find(condition01):
    print(i)
for i in find(condition02):
    print(i)
for i in find(condition03):
    print(i)
# 方法参数，如果传递10/"张无忌"/ True，叫做传递数据
# 方法参数，如果函数1/函数2/函数3，叫做传递逻辑
