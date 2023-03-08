"""
    生成器表达式
"""

list01 = [3, "54", True, 4556, 6, "76", 1.6, False, 3.5]


# 生成器函数
def find01():
    for i in list01:
        if type(i) == int:
            yield i


re = find01()
for item in re:
    print(item)

# 生成器表达式
# 此时没有计算 ，更没有结果
re = (item for item in list01 if type(item) == int)
# 一次循环，一次计算，一个结果
for item in re:
    print(item)

# 注意与列表推导式的区别，内存占用非常大
# 此时已经完成所有计算，得到所有结果
re_list = [item for item in list01 if type(item) == int]
# 只是获取结果
for item in re_list:
    print(item)

# 变量= [item for item in 可迭代对象 if 条件] 列表推导
# 变量= {k ,v for k,v in 可迭代对象 if 条件} 字典推导
# 变量= {item for item in 可迭代对象 if 条件} 集合推导
# 变量= (itme for item in 可迭代对象 if 条件) 生成器表达式
