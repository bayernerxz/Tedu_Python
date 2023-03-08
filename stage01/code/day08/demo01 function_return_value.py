"""
    函数返回值 语法
    pycharm的快捷键
    Ctrl+P 在调用函数时，在括号内可以显示参数的提示
    Ctrl+Q 在调用函数时，显示整个函数的提示
    Ctrl+click ctrl+鼠标左键单击函数可以定位到函数的定义的代码

"""


# 参数：调用者传递给定义者的信息
# 返回值：定义者传递给调用者的结果
def fun01(a):
    print("fun01执行了")
    # 作用：1.返回结果 2.退出方法
    return 20


# pycharm调试时，F8逐过程step Over（跳过方法）
# pycharm调试时，F7逐过程step Info（进入方法）
re = fun01()
print(re)


# 无返回值函数
def fun02(a):
    print("fun01执行了")


re = fun02(100)
print(re)  # None
