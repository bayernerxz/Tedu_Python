"""
    定义图形管理器类
        1.管理所有图形
        2.提供计算所有图形总面积的方法

    具体图形：
        圆形（pi* r**2）
        矩形（长*宽）
        ...

    测试：
        创建1个圆形对象，1个矩形对象，添加到图形管理器中。
        调用图形管理器的计算面积方法，输出结果。

    要求：增加新图形，不修改图形管理器的代码。
    体会：面向对象三大特征：
            封装/继承/多态
        面向对象设计原则：
            开闭/单一/倒置

"""


class Shape:
    def get_area(self):
        # 如果子类不重写，则异常。
        raise NotImplementedError()


class ShapeManager:
    def __init__(self):
        self.__shapes = []

    def add_shape(self, shape):
        if isinstance(shape, Shape):
            self.__shapes.append(shape)
        else:
            raise ValueError

    def get_total_area(self):
        total_area = 0
        for shape in self.__shapes:
            # 多态
            # 调用的是图形
            # 执行的是圆形/矩形/...
            total_area += shape.get_area()
        return total_area


# --------------------------------
class Circular(Shape):
    def __init__(self, r):
        self.radius = r

    def get_area(self):
        import math
        return self.radius ** 2 * math.pi


class Rectangular(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


if __name__ == "__main__":
    manager = ShapeManager()
    manager.add_shape(Circular(3))
    manager.add_shape(Rectangular(3, 5))
    print(manager.get_total_area())
