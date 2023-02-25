"""
    练习1：将day11/day10-exercise/exercise01.py中的
            Vector2和DoubleListHelper定义到double_list_helper.py模块中。
    练习2：定义exercise.py模块中，实现
        1）在二维列表中，获取13位置，向左，2个元素
        2）在二维列表中，获取22位置，向上，2个元素
        3）在二维列表中，获取03位置，向下，2个元素
    要求：使用三种导入方式
    体会：哪一种更合适
"""
list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]

# import double_list_helper as d
# 
# print(d.DoubleListHelper().get_elements(list01, d.Vector2(0, 3), d.Vector2(1, 0), 2))
# print(d.DoubleListHelper().get_elements(list01, d.Vector2(1, 3), d.Vector2(0, -1), 2))
# print(d.DoubleListHelper().get_elements(list01, d.Vector2(2, 2), d.Vector2(-1, 0), 2))


# from double_list_helper import Vector2 as V
# from double_list_helper import DoubleListHelper as D
# 
# print(D.get_elements(list01, V(1, 3), V(0, -1), 2))
# print(D.get_elements(list01, V(2, 2), V(-1, 0), 2))
# print(D.get_elements(list01, V(0, 3), V(1, 0), 2))


from double_list_helper import *

print(DoubleListHelper().get_elements(list01, Vector2(0, 3), Vector2(1, 0), 2))
print(DoubleListHelper().get_elements(list01, Vector2(1, 3), Vector2(0, -1), 2))
print(DoubleListHelper().get_elements(list01, Vector2(2, 2), Vector2(-1, 0), 2))
