"""
    练习：敌人类（攻击力0-100）
        抛出异常的信息：消息/错误行/攻击力/错误编号
"""


class AtkError(Exception):
    """
        攻击类错误
    """
    def __init__(self, message, code_line, atk, error_number):
        super(AtkError, self).__init__()
        self.message = message
        self.code_line = code_line
        self.atk = atk
        self.error_number = error_number


class Enemy:
    def __init__(self, atk):
        self.atk = atk

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 <= value <= 100:
            self.__atk = value
        else:
            raise AtkError("攻击力范围错误", 27, value, 1001)


try:
    e01 = Enemy(102)
except AtkError as ae:
    print(ae.message)
    print(str(ae.atk) + "超出范围")
    print("错误位于" + str(ae.code_line) + "行")
    print("错误类型是" + str(ae.error_number))
