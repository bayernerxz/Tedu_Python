"""
list-->str
"""

# 需求：根据xx逻辑，拼接一个字符串。
# “0123456789”
# 缺点：每一次拼接循环，都会生成一个新的字符串对象，替换变量引用result
# result = ""
# for i in range(10):
#     # ""
#     # "0"
#     # "01"
#     # "012"
#     result += str(i)

# 优点：每次循环只向列表添加字符串，没有创建列表对象
list_temp = []
for i in range(10):
    list_temp.append(str(i))
# join: list-->str
# result="连接符".join(列表)
result = "".join(list_temp)

print(result)
