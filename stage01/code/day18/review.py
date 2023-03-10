"""
    复习
    面向对象编程：考虑问题从对象的角度出发
    函数式编程：考虑问题从函数的角度出发
        “封装”：封装变化点
        “继承”：抽象变化/隔离变化
        “多态”：调用抽象的函数变量，执行具体的个性函数

        lambda：匿名方法，作为实参
"""

"""  思想
def 功能1():
    共性代码
    个性1代码

def 功能2():
    共性代码
    个性2代码

def 功能3():
    共性代码
    个性3代码

“封装”...
def 个性1():
    个性1代码

def 个性2():
    个性2代码

def 个性3():
    个性3代码

# 继承
# 指向函数类型的变量就是具体个性函数的抽象
def 共性(指向函数类型的变量):
    共性代码
    # 多态
    指向函数类型的变量() --> 执行具体个性代码

执行...
共性(个性1)
共性(个性2)
共性(个性3)
"""

"""项目
将共性代码提取到单独的模块中。
在某个代码中导入模块，定义个性代码，调用静态方法（共性代码）
from common.list_helper import *

def 个性代码():
    ...
    
结果 = ListHelper.静态方法(要操作的数据, 个性代码)
"""

"""lambda
lambda element:item.id==101

def 方法名(参数):
    函数体
    
结果 = ListHelper.静态方法(要操作的数据, lambda)
"""
