from time import sleep
from threading import Thread, Lock


# 交易类
class Account:
    def __init__(self, _id, balance, lock):
        self.id = _id  # 用户
        self.balance = balance  # 存款
        self.lock = lock  # 锁

    # 取钱
    def withdraw(self, amount):
        self.balance -= amount

    # 存钱
    def deposit(self, amount):
        self.balance += amount

    # 查看余额
    def get_balance(self):
        return self.balance


# 产生两个账户
tom = Account("Tom", 5000, Lock())
alex = Account("Alex", 8000, Lock())


# 转账过程
def transfer(from_, to, amount):
    if from_.lock.acquire():  # 锁住自己账户  # 在同时互相转账时，将账户都上锁
        from_.withdraw(amount)  # 账户减少
        sleep(0.5)
        if to.lock.acquire():  # 对方账户上锁   # 在同时互相转账时，已经上锁的账户再上锁，会导致两个线程都阻塞。
            to.deposit(amount)  # to账户加钱
            to.lock.release()  # to解锁
        from_.lock.release()  # from账户解锁
    print("%s给%s转账%d" % (from_.id, to.id, amount))


t1 = Thread(target=transfer, args=(tom, alex, 2000))
t2 = Thread(target=transfer, args=(alex, tom, 3000))
t1.start()
t2.start()
t1.join()
t2.join()
