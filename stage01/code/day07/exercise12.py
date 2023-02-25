# 练习：将下列代码，定义到函数中，再调用一次。
def print_rectangle(row, column, char):
    """
    打印矩形
    :param row: 行数
    :param column: 列数
    :param char: 打印的组成字符
    """
    for r in range(row):
        for c in range(column):
            print(char, end=" ")
        print()


print_rectangle(5, 4, "/")
