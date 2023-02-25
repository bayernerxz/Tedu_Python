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
    def get_elements(target, pos, direction, count):
        list_result = []
        for i in range(count):
            pos.x += direction.x
            pos.y += direction.y
            element = target[pos.x][pos.y]
            list_result.append(element)
        return list_result
