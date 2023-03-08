"""
    运算符重载
"""


class Vector1:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"一维向量的分量是：{self.x}"

    def __add__(self, other):
        return Vector1(self.x + other)

    def __radd__(self, other):
        return Vector1(self.x + other)

    def __mul__(self, other):
        return Vector1(self.x * other)

    def __sub__(self, other):
        return Vector1(self.x - other)

    def __rmul__(self, other):
        return Vector1(self.x * other)

    def __rsub__(self, other):
        return Vector1(other - self.x)

    def __iadd__(self, other):
        self.x += other
        return self


v01 = Vector1(10)
print(v01 + 2)  # v01.__add__(2)
# 练习：实现自定义类的对象与数值的减法，乘法运算。
# 略

print(3 + v01)  # v01.__add__(2)
# 练习：实现数值与自定义类的对象的减法，乘法运算。
# 略

# 重写__iadd__，实现在原对象基础上的变化
# 如果不重写__iadd__，默认使用__add__，一般会产生新对象。
v01 += 2
print(v01, id(v01))

# list01 = [1]
# print(id(list01))
# # 生成新对象
# re = list01 + [2]
# print(re, id(re))
# # 在原有对象基础，累加
# list01 += [2]
# print(list01, id(list01))
