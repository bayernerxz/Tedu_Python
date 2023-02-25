# 练习2: 定义根据两，计算几斤零几两的函数

def calc_jin_liang(liangs):
    """
    根据两，计算几斤零几两
    :param liangs:总共多少两
    :return: 元组(斤,两)
    """
    jin = liangs // 16
    liang = liangs % 16
    return jin, liang


print("%d斤%d两" % calc_jin_liang(20))
