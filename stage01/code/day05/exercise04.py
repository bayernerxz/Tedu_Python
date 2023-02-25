"""
练习1：
    将列表[54,25,13,23,43,35,17]中,所有大于30的数字存入另外一个列表
    并画出内存图

练习2：
    在控制台中录入5个数字,打印最大值（不使用max()函数）
"""

list01 = [54, 25, 13, 23, 43, 35, 17]
list02 = []
for i in list01:
    if i > 30:
        list02.append(i)
print(list02)

list_number = [int(input("请输入第1个数字："))]
max_number = list_number[0]
for i in range(4):
    temp_number = int(input(f"请输入第{i + 2}数字："))
    list_number.append(temp_number)
    if temp_number >= max_number:
        max_number = temp_number
print(f"最大的数字是：{max_number}")
