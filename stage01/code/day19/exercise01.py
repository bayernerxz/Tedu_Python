"""
    练习：在不改变原有功能（存取钱）的定义与调用情况下，增加验证账号的功能。
"""


def verify(func):
    def wrapper(*args, **kwargs):
        print("验证账号")
        return func(*args, **kwargs)

    return wrapper


@verify
def deposit(money):
    print("存了%d的钱" % money)


@verify
def withdraw(login_id, pwd):
    print("取钱喽", login_id, pwd)


deposit(10000)
withdraw("张三", 123)
