# 练习：
a = "A"
b = "B"
# 将变量b存储的地址赋值给变量a
a = b
b = "C"
print("变量a是" + a)  # "B"

# 练习2：
# 在控制台中获取两个变量，然后交换数据，最后显示结果。
# “请输入第一个变量：”
# “请输入第二个变量：”
#         交换
# “第一个变量是：”
# “第二个变量是：”

data01 = input("请输入第一个变量：")
data02 = input("请输入第二个变量：")
# 版本1：所有语言通用思想
# temp = data01
# data01 = data02
# data02 = temp
# 版本2：适合python
data01, data02 = data02, data01
print("第一个变量是：" + data01)
print("第二个变量是：" + data02)
