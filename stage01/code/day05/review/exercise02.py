"""
4、在控制台中获取一个整数作为边长，根据边长打印矩形。
    例如：4
        ****
        *  *
        *  *
        ****

        6
        ******
        *    *
        *    *
        *    *
        *    *
        ******
"""

slide = int(input("请输入整数边长："))
if slide <= 1:
    print("输入错误，请输入大于1的整数")
print("*" * slide)
for item in range(slide - 2):
    print("*" + " " * (slide - 2) + "*")
print("*" * slide)
