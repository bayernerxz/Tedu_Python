from threading import Thread
from time import sleep, ctime


class MyThread(Thread):
    def __init__(self, target, args, kwargs):
        super().__init__()  # 此行不许传参
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        # 执行self.target函数
        self.target(*self.args, **self.kwargs)


############################################
def player(sec, song):
    for i in range(3):
        print("Playing %s : %s" % (song, ctime()))
        sleep(sec)


t = MyThread(target=player, args=(3,), kwargs={"song": "凉凉"})
t.start()
t.join()
