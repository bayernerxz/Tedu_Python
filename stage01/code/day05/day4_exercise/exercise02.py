"""
在控制台中获取一个整数作为边长。根据边长打印矩形
例如：4
        ****
        *  *
        *  *
        ****
"""

side_length = int(input("请输入一个整数作为边长："))
print("*" * side_length)
for i in range(side_length - 2):
    print("*" + " " * (side_length - 2) + "*")
print("*" * side_length)
