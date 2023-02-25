# 作业：调用fun07

def fun07(a, b, *args, c, d, **kwargs):
    pass


#    /位置  /星号元组          /命名关键字(默认)   /双星号字典
fun07(1, 2, "asdf", 34, True, c=15, d="sasdf", e="25", f="35")


def fun01(*args, **kwargs):
    print(args)
    print(**kwargs)


fun01(1, 2, 3, 4, a=1, b=3)
