"""
    自定义异常类
"""


class AgeError(Exception):
    """
        年龄错误
    """

    def __init__(self, message, age_value, code_line, error_number):
        # super().__init__(message)  # 这个地方传递的message是出现在报错信息最下方的提示，写与不写都可以。
        self.message = message
        self.age_value = age_value
        self.code_line = code_line
        self.error_number = error_number


class Wife:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 21 <= value <= 31:
            self.__age = value
        else:
            # 多个错误信息，用类把多个错误信息封闭成一个
            # raise ValueError("我不要")
            raise AgeError("超过我想要的范围", value, 26, 1001)


try:
    w01 = Wife(81)
except AgeError as e:
    print("请重新输入:")
    print(e.age_value, e.error_number, e.code_line, e.message)
