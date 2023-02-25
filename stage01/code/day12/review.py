"""
    day12 复习
    封装
        数据角度：将多个变量封闭到一个自定义类中。
                优势：
                    符合人类的思考方式
                    可以将数据与对数据的操作封闭到一起

        功能角度：对外提供必要的功能，隐藏实现的细节。
                DoubleListHelper.get_elements()
                ——私有化：将名称命名为以双下划线开头。
                        内部修改成员名称。
                ——属性(property)：对实例变量的保护（拦截读/写操作）
                ——__slots__：限定类创建的对象只能有固定的实例变量。

        设计角度：
            分而治之：将大的需求分解为多少类，每个类负责一个职责
            变则疏之：遇到变化点，单独封闭为一个类
            ----------------
            高内聚：一个类有则只有一个发生变化的原因
            低耦合：类与类的关系松散

"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # ...

    def print_self(self):
        print(self.name, self.age)


s01 = Student("无忌哥哥", 28)
# 通过对象调用实例成员
s01.name = "张无忌"
s01.print_self()


class Student02:
    def __init__(self, name, age):
        self.name = name
        # self.age = age
        # self.__age = age
        self.set_age(age)
        # ...

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value


class Student03:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.__age = age
        # self.set_age(age)
        # ...

    def __get_age(self):
        return self.__age

    def __set_age(self, value):
        self.__age = value

    age = property(__get_age, __set_age)


s01 = Student03("无忌哥哥", 28)
s01.name = "张无忌"


class Student04:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # 只读
    @property
    def age(self):
        return self.__age


s01 = Student04("无忌哥哥", 28)


# s01.age = 20  # 只读，赋值会报错


class Student05:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 只写
    def set_age(self, value):
        self.__age = value

    age = property(None, set_age)


s05 = Student05("无忌哥哥", 28)


# print(s01.age)  # 只写报错


class Student06:
    def __init__(self, name, age):
        self.name = name
        # 可读可写
        self.age = age

    def __get_age(self):
        return self.__age

    def __set_age(self, value):
        self.__age = value

    age = property(__get_age, __set_age)


s06 = Student06("无忌哥哥", 28)
s06.name = "张无忌"


class Student07:
    __slots__ = ("name",)

    def __init__(self, name):
        self.name = name


s07 = Student07("无忌")
# s07.name = "无忌"
# print(s01.name)

# 添加了新实例变量
s07.nmae = "无忌"  # 写错了的属性也会被存入__dict__
print(s01.name)  # 'Student07' object has no attribute 'nmae'


class Student08:
    __slots__ = ("__age",)

    def __init__(self, age):
        # 可读可写
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value
