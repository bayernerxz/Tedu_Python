"""
    元组
        基础操作
"""

# 1.创建元组
# 空
tuple01 = ()
print(tuple01)
# 具有默认值
tuple01 = (1, 2, 3)
print(tuple01)
# 列表-->元组
tuple01 = tuple(["a", "b"])
# 元组-->列表
list(tuple01)
print(tuple01)

# 如果元组只有一个元素，创建时需要在括号内最后加一个逗号
# tuple02 = (100)
# print(type(tuple02))  # int

tuple02 = (100,)
print(type(tuple02))  # tuple

# 不能变化
# tuple02[0] = 10

# 2.获取元素
tuple03 = ("a", "b", "c", "d")
e01 = tuple03[1]  # str
print(type(e01))
e01 = tuple03[-1:]
print(type(e01))  # tuple

# 可以直接将元组赋值给多个变量
tuple04 = (100, 200)  # 其实列表或字符串或其它容器也可以实现，但一般开发时都使用元组
a, b = tuple04
print(a)
print(b)

# 3.遍历元素
# 正向
for item in tuple04:
    print(item)

# 反向
# 3, 2, 1, 0
for i in range(len(tuple04) - 1, -1, -1):
    print(tuple04[i])
# -1,-2,-3,-4
for i in range(- 1, -len(tuple04) - 1, -1):
    print(tuple04[i])
