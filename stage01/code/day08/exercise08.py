# 练习：记录一个函数的执行次数
#       画出内存图

count = 0


def fun01():
    global count
    count += 1
    pass


fun01()
fun01()
fun01()
fun01()
fun01()
print("调用%d次" % count)
