# 练习:定义函数﹐根据小时,分钟,秒,计算总秒数．#要求∶可以只计算小时-->秒
#       可以只计算分钟-->秒
#       可以只计算小时＋分钟-->秒
#       可以只计算小时＋秒-->秒


def calc_sec(hours=0, minutes=0, seconds=0):
    return 60 * 60 * hours + 60 * minutes + seconds


# 小时﹐分钟﹐秒,
print(calc_sec(1, 1, 1))
# 小时﹐分钟
print(calc_sec(2, 3))
# 分钟﹐秒,
print(calc_sec(minutes=2, seconds=3))
# 小时﹐
print(calc_sec(2))
# 分钟﹐
print(calc_sec(minutes=2))
