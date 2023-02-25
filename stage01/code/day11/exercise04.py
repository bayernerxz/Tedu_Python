"""
    请以面向对象的思想，描述下列场景：
        小明在招商银行取钱
"""


class Depositor:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


class Bank:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def withdrawal_of_money(self, depositor):
        print(f"{depositor.name}在{self.name}取钱")


xm = Depositor("小明")
cmb = Bank("招商银行")
cmb.withdrawal_of_money(xm)
