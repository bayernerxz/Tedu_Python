"""
    定义父类
        动物（行为：叫）

    定义子类
        狗（行为：跑）
        鸟（行为：飞）

    创建三个类型的对象
    体会：isinstance(对象，类型)
    体会：issubclass(类型，类型)
"""


class Animal:
    def shout(self):
        print("叫")


class Dog(Animal):
    def run(self):
        print("跑")


class Bird(Animal):
    def fly(self):
        print("飞")


husky = Dog()
swan = Bird()

print(isinstance(husky, Dog))  # True
print(isinstance(husky, Animal))  # True
print(isinstance(husky, Bird))  # False
print(isinstance(swan, Dog))  # False
print(isinstance(swan, Animal))  # True
print(isinstance(swan, Bird))  # True

print(issubclass(Dog, Bird))  # False
print(issubclass(Dog, Animal))  # True
print(issubclass(Bird, Animal))  # True
print(issubclass(Bird, Dog))  # False
print(issubclass(Animal, Dog))  # False
print(issubclass(Animal, Bird))  # False
