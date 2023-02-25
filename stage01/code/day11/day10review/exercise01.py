"""
3.
[
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]
在二维列表中，获取13位置，向左，2个元素
在二维列表中，获取22位置，向上，2个元素
在二维列表中，获取03位置，向下，2个元素
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def left():
        return Vector2(0, -1)

    @staticmethod
    def right():
        return Vector2(0, 1)

    @staticmethod
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def down():
        return Vector2(1, 0)


class DoubleListHelper:
    @staticmethod
    def get_elements(target, pos, dir, count):
        list_result = []
        for i in range(count):
            pos.x += dir.x
            pos.y += dir.y
            element = target[pos.x][pos.y]
            list_result.append(element)
        return list_result


# -----------测试代码-----------------------
list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]

# 在二维列表中，获取13位置，向左，2个元素
print(DoubleListHelper.get_elements(list01, Vector2(1, 3), Vector2.left(), 2))
# 在二维列表中，获取22位置，向上，2个元素
print(DoubleListHelper.get_elements(list01, Vector2(2, 2), Vector2.up(), 2))
# 在二维列表中，获取03位置，向下，2个元素
print(DoubleListHelper.get_elements(list01, Vector2(0, 3), Vector2.down(), 2))
