"""
    复习：
    迭代
        可迭代对象
        迭代器
    生成器


class 可迭代对象：
    def __iter__():
        创建迭代器对象

class 迭代器对象：
    def __next__():
        返回一个元素
        如果没有元素，则抛出一个StopIteration异常。

for 变量 in 可迭代对象：
    变量得到的就是__next__()方法返回值

原理：
iterator = 可迭代对象.__iter__()
while True:
    try:
        变量 = iterator.__next__()
    except:
        break

启发：调用next执行一次，计算一次，返回一次

协程：第二阶段讲授

生成器函数：
def 函数名():
    ...
    yield 数据
    ...

变量=函数名()
# for 生成器，才执行函数体
for item in 生成器：
    ...

优势：延迟/惰性操作

生成器源代码

class 生成器：
    def __iter__(self):
        return self

    def __next__(self):
        定义着yield以前的代码
        返回yield后面的数据

"""


