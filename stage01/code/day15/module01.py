# 定义：当前模块哪些成员可以被from 模块 improt * 导入
__all__ = ["fun01", "MyClass", "_fun02"]

print("模块1")


def fun01():
    print("module1 - fun01")


# 只是在模块内部使用的成员，可以以单下划线开关。
# 只限于from 模块 improt *有用。
def _fun02():
    print("module1 - fun02")


class MyClass:
    @staticmethod
    def fun03():
        print("module1 - fun03")

print(__name__)